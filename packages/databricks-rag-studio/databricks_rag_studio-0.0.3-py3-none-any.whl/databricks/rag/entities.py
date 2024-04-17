import string
from abc import ABC
from dataclasses import dataclass
from enum import Enum
from itertools import chain
from typing import Optional, Dict, List, Mapping, Any, Iterable

import yaml

from databricks.rag import constants, errors


# Returns a new dictionary with all keys except the ones specified in `keys` removed.
def _without_keys(input_dict: Mapping[str, Any], keys: Iterable[str]) -> Dict:
    return {k: input_dict[k] for k in input_dict.keys() - set(keys)}


# Entity class to encode the following yaml
# data_ingestors:
#     - name: spark-docs-ingestor
#         description: Ingest Spark docs from the website
#         # Optional.  The Unity Catalog Volume where the raw docs are stored.  If not specified, will default to `{name}__raw_docs`
#         destination_uc_volume: raw-spark-docs
@dataclass
class DataIngestor:
    name: str
    description: str
    destination_uc_volume: Optional[str] = None

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "DataIngestor":
        data_ingestor = cls(**config)
        if data_ingestor.destination_uc_volume is None:
            data_ingestor.destination_uc_volume = f"{data_ingestor.name}__raw_docs"
        return data_ingestor


# Entity class to encode the following yaml
# data_processors:
#     - name: spark-docs-processor
#     description: Parse, chunk, embed Spark documentation
#     # explicit link to the data ingestors that this processor uses.
#     data_ingestors:
#         - name: spark-docs-ingestor
#     # Optional.  The Unity Catalog table where the embedded, chunked docs are stored.
#     # If not specified, will default to `{name}__embedded_docs__{version_number}`
#     # If specified, will default to `{provided_value}__{version_number}`
#     destination_table:
#         name: spark-docs-chunked
#     destination_vector_index:
#         databricks_vector_search:
#             # Optional.  The Unity Catalog table where the embedded, chunked docs are stored.
#             # If not specified, will default to `{name}__embedded_docs_index__{version_number}`
#             # If specified, will default to `{provided_value}__{version_number}`
#             index_name: spark-docs-chunked-index
#     embedding_model:
#         endpoint_name: databricks-bge-large-en
#         instructions:
#             embedding: "Represent this sentence for searching relevant passages:"
#             query: ""
#     # these are key-value pairs that can be specified by the end user
#     configurations:
#         - chunk_size: 500
#         - chunk_overlap: 50


class RagStudioEntity:
    @classmethod
    def _find(cls, haystack: List[Dict[str, str]], needle: str, default_value: str):
        for stack in haystack:
            if needle in stack:
                return stack[needle]
        return default_value


@dataclass
class EmbeddingTable(RagStudioEntity):
    name: Optional[str] = None

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "EmbeddingTable":
        # TODO: set default value if not specified
        provided_name = config.get("name", "")
        return cls(name=provided_name)


@dataclass
class VectorIndex(RagStudioEntity):
    name: str

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "VectorIndex":
        # TODO: set default value if not specified
        provided_name = config.get("databricks_vector_search", {}).get("index_name", "")
        return cls(name=provided_name)


@dataclass
class EmbeddingModel(RagStudioEntity):
    endpoint_name: str
    embedding_instructions: str = ""
    query_instructions: str = ""

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "EmbeddingModel":
        INSTRUCTIONS = "instructions"
        instructions = config.get(INSTRUCTIONS, {})
        return cls(
            **_without_keys(config, [INSTRUCTIONS]),
            embedding_instructions=instructions.get("embedding", ""),
            query_instructions=instructions.get("query", ""),
        )


@dataclass
class DataProcessor:
    name: str
    description: str
    data_ingestors: List[str]
    destination_table: Optional[EmbeddingTable] = None
    destination_vector_index: Optional[VectorIndex] = None
    embedding_model: Optional[EmbeddingModel] = None
    configurations: Optional[Dict] = None

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "DataProcessor":
        DESTINATION_TABLE = "destination_table"
        DESTINATION_VECTOR_INDEX = "destination_vector_index"
        EMBEDDING_MODEL = "embedding_model"

        destination_table = config.get(DESTINATION_TABLE, {})
        destination_vector_index = config.get(DESTINATION_VECTOR_INDEX, {})
        embedding_model = config.get(EMBEDDING_MODEL, {})
        data_processor = cls(
            **_without_keys(
                config, [DESTINATION_TABLE, DESTINATION_VECTOR_INDEX, EMBEDDING_MODEL]
            ),
            destination_table=EmbeddingTable.from_config(destination_table),
            destination_vector_index=VectorIndex.from_config(destination_vector_index),
            embedding_model=EmbeddingModel.from_config(embedding_model),
        )
        return data_processor

    def get_configurations(self) -> Dict[str, str]:
        return self.configurations or {}


# Create an enum that could have possible values "system", "assistant" and "user"
class Role(Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"


@dataclass
class Message:
    role: Role
    content: str

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "Message":
        ROLE = "role"
        return cls(
            **_without_keys(config, [ROLE]),
            role=Role(config[ROLE]),
        )


@dataclass
class ChatMessage:
    messages: List[Message]

    @classmethod
    def from_config(cls, config: List) -> "ChatMessage":
        messages = list(
            map(
                lambda message: Message.from_config(message),
                config,
            )
        )
        return cls(messages)


@dataclass
class PromptTemplate:
    chat_messages: ChatMessage
    template_string: Optional[str] = None
    template_variables: Optional[List[str]] = None

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "PromptTemplate":
        chat_messages = ChatMessage.from_config(config.get("chat_messages"))
        template_string = "\n".join(
            [chat_message.content for chat_message in chat_messages.messages]
        )
        template_variables = [
            field_name
            for _, field_name, _, _ in string.Formatter().parse(template_string)
            if field_name
        ]

        return cls(
            chat_messages,
            template_string,
            template_variables,
        )


# Entity class to encode the following YAML
# retrievers:
#     - name: ann-retriever
#     description: Basic ANN retriever
#     # explicit link to the data processor that this retriever uses.
#     data_processors:
#         - name: spark-docs-processor
#     # these are key-value pairs that can be specified by the end user
#     configurations:
#         k: 5
#         use_mmr: false
@dataclass
class Retriever:
    name: str
    description: str
    data_processors: List[DataProcessor]
    configurations: Optional[Dict] = None

    @classmethod
    def from_config(
        cls,
        config: Mapping[str, Any],
        *,
        data_processors_values: Iterable[Mapping[str, Any]],
    ) -> "Retriever":
        DATA_PROCESSORS = "data_processors"

        data_processors = config.get(DATA_PROCESSORS, [])
        data_processors_mapping = {
            data_processor["name"]: data_processor
            for data_processor in data_processors_values
        }
        data_processor_list = [
            DataProcessor.from_config(
                data_processors_mapping.get(data_processor["name"])
            )
            for data_processor in data_processors
        ]
        return cls(
            **_without_keys(config, [DATA_PROCESSORS]),
            data_processors=data_processor_list,
        )


# Entity class to encode the following YAML
# chains:
#     - name: spark-docs-chain # User specified, must be unique, no spaces
#     description: Spark docs chain # User specified, any text string
#     # explicit link to the retriever that this chain uses.
#     # currently, only one retriever per chain is supported, but this schema allows support for adding multiple in the future
#     retrievers:
#         - name: ann-retriever
#     foundational_models:
#         - name: llama-2-70b-chat # user specified name to reference this model in the chain & to override per environment.  Must be unique.
#         type: v1/llm/chat
#         endpoint_name: databricks-llama-2-70b-chat
#         prompt_template:
#             chat_messages:
#                 - role: "system"
#                     content: "You are a smart assistant made by Databricks Spark"
#                 - role: "user"
#                     content: "Respond to {query} based on {docs}..."
#     # Optional.  The Unity Catalog name of the logged model.
#     # If not specified, will default to `{name}__chain__{version_number}`
#     # If specified, will default to `{provided_value}__{version_number}`
#     destination_model_name: spark-docs-chain
#     # these are key-value pairs that can be specified by the end user
#     configurations:
#         - sample_config_setting: false


@dataclass
class FoundationModel(RagStudioEntity):
    name: str
    type: str
    endpoint_name: str
    prompt_template: PromptTemplate
    configurations: Optional[Dict] = None

    @classmethod
    def from_config(cls, config: Mapping[str, Any]) -> "FoundationModel":
        PROMPT_TEMPLATE = "prompt_template"
        prompt_template = config.get(PROMPT_TEMPLATE, {})
        return cls(
            **_without_keys(config, [PROMPT_TEMPLATE]),
            prompt_template=PromptTemplate.from_config(prompt_template),
        )


@dataclass
class Chain:
    name: str
    description: str
    retrievers: List[Retriever]
    foundational_models: List[FoundationModel]

    @classmethod
    def from_config(
        cls,
        config: Mapping[str, Any],
        *,
        data_processors_values: Iterable[Mapping[str, Any]],
        retriever_values: Iterable[Mapping[str, Any]],
    ) -> "Chain":
        RETRIEVERS = "retrievers"
        FOUNDATIONAL_MODELS = "foundational_models"

        retrievers = config.get(RETRIEVERS, [])
        retrievers_mapping = {
            retriever["name"]: retriever for retriever in retriever_values
        }
        retriever_list = [
            Retriever.from_config(
                retrievers_mapping.get(retriever["name"]),
                data_processors_values=data_processors_values,
            )
            for retriever in retrievers
        ]

        foundational_models = list(
            map(
                lambda foundational_model: FoundationModel.from_config(
                    foundational_model
                ),
                config.get(FOUNDATIONAL_MODELS, []),
            )
        )
        return cls(
            **_without_keys(config, [RETRIEVERS, FOUNDATIONAL_MODELS]),
            retrievers=retriever_list,
            foundational_models=foundational_models,
        )


@dataclass(init=False, repr=False, frozen=True)
class UnityCatalogEntity(ABC):
    """Abstraction for Unity Catalog Entity, such as Table, Volume, Model, Vector Search Index"""

    catalog_name: str
    schema_name: str

    _entity_name: str
    """
    Name of the entity.
    Given the fully-qualified name "a.b.c" then this method should return "c".
    For each UC entity type, it has different meaning, such as table_name, volume_name, model_name, index_name etc.
    """

    def __init__(self, catalog_name: str, schema_name: str, entity_name: str):
        super().__init__()
        # We set frozen=True in the dataclass decorator, so we need to use object.__setattr__ to set the attributes
        object.__setattr__(
            self,
            "catalog_name",
            UnityCatalogEntity._unsanitize_identifier(catalog_name),
        )
        object.__setattr__(
            self, "schema_name", UnityCatalogEntity._unsanitize_identifier(schema_name)
        )
        object.__setattr__(
            self, "_entity_name", UnityCatalogEntity._unsanitize_identifier(entity_name)
        )

    @classmethod
    def from_full_name(cls, full_name: str):
        identifiers = full_name.split(".")
        if len(identifiers) != 3:
            raise ValueError(
                f"Qualified UC entity full name {full_name} should be in the format 'catalog.schema.entity'"
            )
        catalog_name, schema_name, entity_name = identifiers
        return cls(catalog_name, schema_name, entity_name)

    def _get_sanitized_catalog_name(self) -> str:
        """Get the sanitized catalog name."""
        return UnityCatalogEntity._sanitize_identifier(self.catalog_name)

    def _get_sanitized_schema_name(self) -> str:
        """Get the sanitized schema name."""
        return UnityCatalogEntity._sanitize_identifier(self.schema_name)

    def _get_sanitized_entity_name(self) -> str:
        """Get the sanitized entity name."""
        return UnityCatalogEntity._sanitize_identifier(self._entity_name)

    def full_name(
        self, *, use_backtick_delimiters: bool = True, escape: bool = True
    ) -> str:
        """
        Get the full name of a UC entity, optionally using backticks to delimit the identifiers.

        :param use_backtick_delimiters: Whether to use backticks to delimit the identifiers.
        :param escape: (deprecated, use `use_backtick_delimiters`) Whether to use backticks to delimit the identifiers.
        """
        if not escape or not use_backtick_delimiters:
            return f"{self.catalog_name}.{self.schema_name}.{self._entity_name}"
        return f"{self._get_sanitized_catalog_name()}.{self._get_sanitized_schema_name()}.{self._get_sanitized_entity_name()}"

    @staticmethod
    def _sanitize_identifier(identifier: str) -> str:
        """
        Escape special characters and delimit an identifier with backticks.
        For example, "a`b" becomes "`a``b`".
        Use this function to sanitize identifiers such as table/column names in SQL and PySpark.
        """
        return f"`{identifier.replace('`', '``')}`"

    @staticmethod
    def _unsanitize_identifier(identifier: str) -> str:
        """
        Unsanitize an identifier. Useful when we get a possibly sanitized identifier from Spark or
        somewhere else, but we need an unsanitized one.
        Note: This function does not check the correctness of the identifier passed in. e.g. `foo``
        is not a valid sanitized identifier. When given such invalid input, this function returns
        invalid output.
        """
        if len(identifier) >= 2 and identifier[0] == "`" and identifier[-1] == "`":
            return identifier[1:-1].replace("``", "`")
        else:
            return identifier

    def _public_fields(self):
        """
        Get a list of public fields. Public field's name does not start with "_".
        """
        return [a for a in self.__dict__.keys() if not a.startswith("_")]

    @classmethod
    def _properties(cls):
        """
        Get a list of properties.
        """
        return sorted(
            [p for p in cls.__dict__ if isinstance(getattr(cls, p), property)]
        )

    def __repr__(self):
        """
        Get the representation of the object.
        Show only public fields and properties.
        The representation is in the format of `ClassName(field1=value1, field2=value2, ...)`.
        """
        kws = [
            f"{key}={self.__getattribute__(key)!r}"
            for key in chain(self._public_fields(), self._properties())
        ]
        return f"{type(self).__name__}({', '.join(kws)})"


@dataclass(init=False, repr=False, frozen=True)
class UnityCatalogTable(UnityCatalogEntity):
    """Abstraction for Unity Catalog Table"""

    def __init__(self, catalog_name: str, schema_name: str, table_name: str):
        super().__init__(catalog_name, schema_name, table_name)

    @property
    def table_name(self) -> str:
        return self._entity_name

    def get_table_url_in_workspace(self, workspace_url: str) -> str:
        """
        Get the URL for the table in the provided workspace.

        :param workspace_url: URL of the workspace to link to
        :return: URL of the table in the Catalog Explorer
        """
        return f"{workspace_url}/explore/data/{self.catalog_name}/{self.schema_name}/{self.table_name}"


@dataclass(init=False, repr=False, frozen=True)
class UnityCatalogVolume(UnityCatalogEntity):
    """Abstraction for Unity Catalog Volume"""

    def __init__(self, catalog_name: str, schema_name: str, volume_name: str):
        super().__init__(catalog_name, schema_name, volume_name)

    @property
    def volume_name(self) -> str:
        return self._entity_name

    def path(self) -> str:
        return f"/Volumes/{self.catalog_name}/{self.schema_name}/{self.volume_name}"

    def dbfs_path(self) -> str:
        return f"dbfs:{self.path()}"


@dataclass(init=False, repr=False, frozen=True)
class UnityCatalogModel(UnityCatalogEntity):
    """Abstraction for Unity Catalog ML Model"""

    def __init__(self, catalog_name: str, schema_name: str, model_name: str):
        super().__init__(catalog_name, schema_name, model_name)

    @property
    def model_name(self) -> str:
        return self._entity_name


@dataclass(init=False, repr=False, frozen=True)
class UnityCatalogVectorSearchIndex(UnityCatalogEntity):
    """Abstraction for Unity Catalog Vector Search Index"""

    def __init__(self, catalog_name: str, schema_name: str, index_name: str):
        super().__init__(catalog_name, schema_name, index_name)

    @property
    def index_name(self) -> str:
        return self._entity_name


@dataclass
class UCAssetsLocation:
    """Abstraction for `uc_assets_location` section of the config file"""

    catalog: str
    schema: str


@dataclass
class AssessmentJudge:
    """Abstraction for an entry in `assessment_judges` section in the config file"""

    judge_name: str
    endpoint_name: str
    assessments: List[str]


@dataclass
class EvaluationConfig:
    """Abstraction for `evaluation` section of the config file"""

    assessment_judges: List[AssessmentJudge]

    @classmethod
    def from_config(cls, config_dict: Mapping[str, Any]):
        ASSESSMENT_JUDGES = "assessment_judges"
        assessment_judges = [
            AssessmentJudge(**judge) for judge in config_dict[ASSESSMENT_JUDGES]
        ]
        if len(assessment_judges) == 0:
            raise ValueError(f"Empty `{ASSESSMENT_JUDGES}` in input config")
        return cls(assessment_judges=assessment_judges)


@dataclass
class GlobalConfig:
    """Abstraction for `global` section of the config file"""

    name: str
    workspace_url: str
    uc_assets_location: UCAssetsLocation
    vector_search_endpoint: str
    mlflow_experiment_name: str

    @classmethod
    def from_config(cls, config_dict: Mapping[str, Any]):
        UC_ASSETS_LOCATION = "uc_assets_location"
        WORKSPACE_URL = "workspace_url"

        uc_assets_location = UCAssetsLocation(**config_dict[UC_ASSETS_LOCATION])
        workspace_url = config_dict[WORKSPACE_URL]
        # Workspace URL should not contain a trailing slash, otherwise it breaks VectorSearchClient
        if workspace_url.endswith("/"):
            workspace_url = workspace_url[:-1]
        return cls(
            **_without_keys(config_dict, [UC_ASSETS_LOCATION, WORKSPACE_URL]),
            uc_assets_location=uc_assets_location,
            workspace_url=workspace_url,
        )


@dataclass
class ProductionEnvironmentInfo:
    """Abstraction for end_users and reviewers in `environment_config` section in the config file"""

    workspace_folder: str
    secret_scope: str
    secret_key: str
    security_key: Optional[str] = None # This field is deprecated please use `secret_key` instead
    security_scope: Optional[str] = None # This field is deprecated please use `secret_scope` instead


@dataclass
class DeveloperEnvironmentInfo:
    """Abstraction for a development environment in `environment_config` section in the config file"""

    name: str
    workspace_folder: str
    secret_scope: str
    secret_key: str
    security_key: Optional[str] = None # This field is deprecated please use `secret_key` instead
    security_scope: Optional[str] = None # This field is deprecated please use `secret_scope` instead
    cluster_id: Optional[str] = None


def _resolve_secret_scope_key(
    env_name: str, environment_config: Mapping[str, str]
) -> Mapping[str, str]:
    # Check if either 'secret_key' or 'security_key' exists in environment_config
    secret_key = environment_config.get("secret_key") or environment_config.get(
        "security_key"
    )
    if not secret_key:
        raise ValueError(
            f"Neither 'secret_key' nor 'security_key' exists in config for {env_name} environment. At least one should be present."
        )

    # Check if either 'secret_scope' or 'security_scope' exists in environment_config
    secret_scope = environment_config.get("secret_scope") or environment_config.get(
        "security_scope"
    )
    if not secret_scope:
        raise ValueError(
            f"Neither 'secret_scope' nor 'security_scope' exists in config for {env_name} environment. At least one should be present."
        )

    return {
        **environment_config,
        "secret_scope": secret_scope,
        "secret_key": secret_key,
    }


@dataclass
class EnvironmentConfig:
    """Abstraction for `environment_config` section of the config file"""

    end_users: ProductionEnvironmentInfo
    reviewers: ProductionEnvironmentInfo
    development: List[DeveloperEnvironmentInfo]

    @classmethod
    def from_config(cls, config_dict: Mapping[str, Any]):
        return cls(
            end_users=ProductionEnvironmentInfo(
                **_resolve_secret_scope_key(
                    constants.EnvironmentName.END_USERS,
                    config_dict[constants.EnvironmentName.END_USERS],
                )
            ),
            reviewers=ProductionEnvironmentInfo(
                **_resolve_secret_scope_key(
                    constants.EnvironmentName.REVIEWERS,
                    config_dict[constants.EnvironmentName.REVIEWERS],
                )
            ),
            development=[
                DeveloperEnvironmentInfo(
                    **_resolve_secret_scope_key(
                        constants.EnvironmentName.DEVELOPMENT,
                        env,
                    )
                )
                for env in config_dict[constants.EnvironmentName.DEVELOPMENT]
            ],
        )


@dataclass
class Config:
    """Abstraction for the entire config file"""

    global_config: GlobalConfig
    evaluation: EvaluationConfig
    environment_config: EnvironmentConfig
    data_ingestors: List[DataIngestor]
    data_processors: List[DataProcessor]
    retrievers: List[Retriever]
    chains: List[Chain]

    @classmethod
    def from_config(cls, config_dict: Mapping[str, Any]) -> "Config":
        GLOBAL_CONFIG = "global_config"
        EVALUATION_CONFIG = "evaluation"
        ENVIRONMENT_CONFIG = "environment_config"
        DATA_INGESTORS = "data_ingestors"
        DATA_PROCESSORS = "data_processors"
        RETRIEVERS = "retrievers"
        CHAINS = "chains"

        return cls(
            global_config=GlobalConfig.from_config(config_dict[GLOBAL_CONFIG]),
            evaluation=EvaluationConfig.from_config(config_dict[EVALUATION_CONFIG]),
            environment_config=EnvironmentConfig.from_config(
                config_dict[ENVIRONMENT_CONFIG]
            ),
            data_ingestors=[
                DataIngestor.from_config(data_ingestor)
                for data_ingestor in config_dict[DATA_INGESTORS]
            ],
            data_processors=[
                DataProcessor.from_config(data_processor)
                for data_processor in config_dict[DATA_PROCESSORS]
            ],
            retrievers=[
                Retriever.from_config(
                    config=retriever,
                    data_processors_values=config_dict[DATA_PROCESSORS],
                )
                for retriever in config_dict[RETRIEVERS]
            ],
            chains=[
                Chain.from_config(
                    config=chain,
                    data_processors_values=config_dict[DATA_PROCESSORS],
                    retriever_values=config_dict[RETRIEVERS],
                )
                for chain in config_dict[CHAINS]
            ],
        )

    @classmethod
    def from_file(cls, config_path: str) -> "Config":
        """Parse a configuration file. Raises ConfigParseError if the file does not contain valid YAML.

        Args:
            config_path (str): Path to the configuration file.

        Returns:
            The parsed configuration file as a mapping.
        """
        try:
            with open(config_path, "r") as f:
                config_dict = yaml.safe_load(f)
                return Config.from_config(config_dict)
        except yaml.parser.ParserError as e:
            raise errors.ConfigParseError(e)
