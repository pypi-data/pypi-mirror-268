import mlflow
import base64
import os
import re
import yaml
import tempfile
from typing import Optional, Union, Dict, Any
from contextlib import contextmanager
from mlflow.models import ModelSignature
from mlflow.models.model import ModelInfo
from mlflow.types import DataType
from mlflow.types.schema import Schema, ColSpec, Object, Array, Property
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.workspace import ExportFormat
from databricks.rag.version import VERSION


def _is_in_comment(line, start):
    """
    Check if the code at the index "start" of the line is in a comment.

    Limitations: This function does not handle multi-line comments, and the # symbol could be in a
    string, or otherwise not indicate a comment.
    """
    return "#" in line[:start]


def _is_in_string_only(line, search_string):
    """
    Check is the search_string

    Limitations: This function does not handle multi-line strings.
    """
    # Regex for matching double quotes and everything inside
    double_quotes_regex = r"\"(\\.|[^\"])*\""

    # Regex for matching single quotes and everything inside
    single_quotes_regex = r"\'(\\.|[^\'])*\'"

    # Regex for matching search_string exactly
    search_string_regex = rf"({re.escape(search_string)})"

    # Concatenate the patterns using the OR operator '|'
    # This will matches left to right - on quotes first, search_string last
    pattern = (
        double_quotes_regex + r"|" + single_quotes_regex + r"|" + search_string_regex
    )

    # Iterate through all matches in the line
    for match in re.finditer(pattern, line):
        # If the regex matched on the search_string, we know that it did not match in quotes since
        # that is the order. So we know that the search_string exists outside of quotes (at least once).
        if match.group() == search_string:
            return False
    return True


# TODO (ML-39713): Improve validation of unsupported code
def _validate_code_content(content_str) -> None:
    """
    Validate that there isn't any code that would work in Databricks but not as exported Python file.
    For now, this only checks for references to 'dbutils'.
    """
    error_message = (
        "The file specified by 'code_path' uses 'dbutils' command which are not supported in a chain model. "
        "To ensure your code functions correctly, remove or comment out usage of 'dbutils' command."
    )

    for line in content_str.splitlines():
        for match in re.finditer(r"\bdbutils\b", line):
            start = match.start()
            if not _is_in_comment(line, start) and not _is_in_string_only(
                line, "dbutils"
            ):
                raise ValueError(error_message)


def _get_temp_file_with_content(file_name: str, content: str, content_format) -> str:
    """
    Write the contents to a temporary file and return the path to that file.

    :param file_name: The name of the file to be created.
    :param content: The contents to be written to the file.

    :return: The string path to the file where the chain model is build.
    """
    # Get the temporary directory path
    temp_dir = tempfile.gettempdir()

    # Construct the full path where the temporary file will be created
    temp_file_path = os.path.join(temp_dir, file_name)

    # Create and write to the file
    with open(temp_file_path, content_format) as tmp_file:
        tmp_file.write(content)

    return temp_file_path


def _get_code(code_path: str) -> str:
    """
    Use the chain file notebook path and convert to python file.
    Here we get the contents using workspace client, write the contents
    to a temporary chain.py file and return the path to that file.

    :param code_path: The string notebook path to the file where the chain
                       model is build.

    :return: The string python path to the file where the chain model is build.
    """
    w = WorkspaceClient()
    response = w.workspace.export(path=code_path, format=ExportFormat.SOURCE)
    decoded_content = base64.b64decode(response.content)
    _validate_code_content(decoded_content.decode("utf-8"))

    return _get_temp_file_with_content("chain.py", decoded_content, "wb")


@contextmanager
def _start_run_or_reuse_active_run():
    """
    Context manager that:
     - returns the active run ID, if exists
     - otherwise start a new mlflow run, and return the run id.
    """
    active_run = mlflow.active_run()
    if active_run:
        yield active_run.info.run_id
    else:
        with mlflow.start_run() as run:
            yield run.info.run_id


# This function serves as a monkey patch for the `_load_code_model` method
# in the `mlflow.langchain` module. Its primary goal is to circumvent the issue of
# Python's module caching mechanism, which by default, prevents the re-importation
# of previously loaded modules. This is particularly problematic in contexts where
# it's necessary to reload a module (in this case, the `chain` module) multiple times
# within the same Python runtime environment.
# The issue at hand arises from the desire to import the `chain` module multiple times
# during a single runtime session. Normally, once a module is imported, it's added to
# `sys.modules`, and subsequent import attempts retrieve the cached module rather than
# re-importing it.
# To address this, the function dynamically imports the `chain` module under unique,
# dynamically generated module names. This is achieved by creating a unique name for
# each import using a combination of the original module name and a randomly generated
# UUID. This approach effectively bypasses the caching mechanism, as each import is
# considered as a separate module by the Python interpreter.
def _fix_load_code_model(code_path=None):
    import importlib.util
    import sys
    import uuid

    with mlflow.langchain._config_path_context(code_path):
        module_name = "chain"

        # here we are using the module_path as sys.path[0] and chain.py
        # to import the chain module since MLflow prepends the module directory
        # of the chain model to sys.path
        module_path = os.path.join(sys.path[0], "chain.py")
        try:
            new_module_name = f"{module_name}_{uuid.uuid4().hex}"
            spec = importlib.util.spec_from_file_location(new_module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[new_module_name] = module
            spec.loader.exec_module(module)
        except ImportError as e:
            raise mlflow.MlflowException("Failed to import LangChain model.") from e

    return mlflow.langchain._rag_utils.__databricks_rag_chain__


def log_model(
    *,
    code_path: str,
    config: Optional[Union[str, Dict[str, Any]]] = None,
    **kwags,
) -> ModelInfo:
    """
    Logs chain code (located at the specified ``code_path``) and configurations.

    :param code_path: The string notebook or file path to the chain code.
    :param config: Python dictionary or path to the configs used to build the chain model.

    :return: A ModelInfo instance that contains the metadata of the logged model.

    Example:

    ```

    from databricks import rag_studio

    model = rag_studio.log_model(
        code_path="ai-bot/chain.py",
        config="ai-bot/chain_config.yml",
    )

    question = {
        "messages": [
            {
                "role": "user",
                "content": "What is Retrieval-augmented Generation?",
            }
        ]
    }

    model.invoke(question)

    ```

    """
    import langchain
    import langchain_core
    import langchain_community
    import databricks.vector_search

    config_path = kwags.get("config_path", None)
    if config_path is not None and (
        not isinstance(config_path, str) or not os.path.exists(config_path)
    ):
        raise ValueError(f"Chain config file {config_path} does not exist")

    if config is not None:
        if config_path is not None:
            raise ValueError(
                "Cannot specify both 'config' and 'config_path' arguments."
            )

        if isinstance(config, str):
            # This is a file path. Validate that it exists
            if not os.path.exists(config):
                raise ValueError(f"Chain config file {config} does not exist")
            config_path = config
        elif isinstance(config, Dict):
            # This is a dictionary. Write it to a temporary YAML file
            config_path = _get_temp_file_with_content(
                "config.yml", yaml.dump(config), "w"
            )
        else:
            raise ValueError(
                f"Invalid argument type for config {config}. Must be a file path or a dictionary"
            )

    if not os.path.exists(code_path) or not isinstance(code_path, str):
        raise ValueError(f"Chain file {code_path} does not exist")

    with _start_run_or_reuse_active_run():
        desired_chain_path = _get_code(code_path)
        input_example = {
            "messages": [
                {
                    "role": "user",
                    "content": "What is Retrieval-augmented Generation?",
                }
            ]
        }
        signature = ModelSignature(
            inputs=Schema(
                [
                    ColSpec(
                        type=Array(
                            Object(
                                [
                                    Property("role", DataType.string),
                                    Property("content", DataType.string),
                                ]
                            ),
                        ),
                        name="messages",
                    )
                ]
            ),
            outputs=Schema(
                [
                    ColSpec(name="id", type=DataType.string),
                    ColSpec(name="object", type=DataType.string),
                    ColSpec(name="created", type=DataType.long),
                    ColSpec(name="model", type=DataType.string),
                    ColSpec(name="choices", type=DataType.string),
                    ColSpec(name="usage", type=DataType.string),
                ]
            ),
        )

        mlflow.langchain._load_code_model = _fix_load_code_model
        return mlflow.langchain.log_model(
            lc_model=desired_chain_path,
            artifact_path="chain",
            pip_requirements=[
                f"mlflow=={mlflow.__version__}",
                f"langchain=={langchain.__version__}",
                f"langchain-core=={langchain_core.__version__}",
                f"langchain-community=={langchain_community.__version__}",
                f"databricks-vectorsearch=={databricks.vector_search.__version__}",
                f"https://ml-team-public-read.s3.us-west-2.amazonaws.com/wheels/rag-serving/uqr082kj-3c87-40b1-b04c-bb1977254aa3/databricks_rag_serving-{VERSION}-py3-none-any.whl",
            ],
            signature=signature,
            input_example=input_example,
            example_no_conversion=True,
            code_paths=[config_path] if config_path else [],
        )
