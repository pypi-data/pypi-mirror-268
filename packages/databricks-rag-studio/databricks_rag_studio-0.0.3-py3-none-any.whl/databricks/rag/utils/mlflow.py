"""
Helper functions to interact with MLflow.
TODO (vperiyasamy): Move this to a separate package dedicated to Databricks services.
"""

import mlflow
from mlflow import MlflowClient
from mlflow.entities.run import Run
import json

from databricks.rag.constants import MLFLOW_EVAL_DATASET_VERSION_TAG


def get_latest_model_version(model_name: str) -> int:
    """
    Get the latest model version for a given model name.

    :param model_name: The name of the model.

    :return: The latest model version.
    """
    mlflow.set_registry_uri("databricks-uc")
    mlflow_client = MlflowClient()
    latest_version = 0
    for mv in mlflow_client.search_model_versions(f"name='{model_name}'"):
        version_int = int(mv.version)
        if version_int > latest_version:
            latest_version = version_int
    return latest_version


def get_run_from_model(model_name, model_version) -> Run:
    """
    Gets the run associated with the specified model version

    :param model_name: The name of the model to get the run for
    :param model_version: The version of the model to get the run for

    :return: The run associated with the specified model version
    """
    mlflow.set_registry_uri("databricks-uc")
    client = MlflowClient()

    model = client.get_model_version(model_name, model_version)
    return client.get_run(model.run_id)


def get_dataset_version(eval_dataset_name):
    """
    Get the version of the eval dataset used.

    :param eval_dataset_name: The name of the eval dataset

    :return: The version of the eval dataset used
    """
    from mlflow.data.spark_delta_utils import (
        _try_get_delta_table_latest_version_from_table_name,
    )

    return _try_get_delta_table_latest_version_from_table_name(eval_dataset_name)


def get_model_uri(model_name: str, model_version: str) -> str:
    """
    Get the model URI for a given model name and version.

    :param model_name: The name of the model.
    :param model_version: The version of the model.
    :return: The model URI.

    :raises ValueError: If model_name or model_version is not provided.
    """
    if not model_name or not model_version:
        raise ValueError(
            "Both model_name and model_version must be provided and non-empty."
        )

    return f"models:/{model_name}/{model_version}"


def update_dataset_version_state(experiment_id, eval_dataset_version):
    """
    Update the state of the eval dataset version for a given experiment. If the eval dataset version is the same as the previous one, then the write mode is append. Otherwise, the write mode is overwrite.

    :param experiment_id: The id of the experiment to update the eval dataset version state for
    :param eval_dataset_version: The version of the eval dataset used

    :return: The write mode to use for the eval dataset version
    """
    client = MlflowClient()
    # TODO (prithvi): handle error when getting experiment
    current_experiment_tags = client.get_experiment(experiment_id).tags

    eval_dataset_version_state = json.loads(
        current_experiment_tags.get(MLFLOW_EVAL_DATASET_VERSION_TAG, "{}")
    )
    previous_eval_dataset_version = eval_dataset_version_state.get("eval_dataset_name")
    write_mode = (
        "append"
        if (
            previous_eval_dataset_version
            and previous_eval_dataset_version == eval_dataset_version
        )
        else "overwrite"
    )
    eval_dataset_version_state["eval_dataset_name"] = eval_dataset_version
    # TODO (prithvi): handle error when setting experiment tag
    client.set_experiment_tag(
        experiment_id,
        MLFLOW_EVAL_DATASET_VERSION_TAG,
        json.dumps(eval_dataset_version_state),
    )
    return write_mode
