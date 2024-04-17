"""
NOTE: Code in this package will be deployed in the scoring server of the RAG Studio app.
It is imperative that we keep the dependencies and imports of this package to a minimum
in order to reduce the size of the model image being served by the endpoint.

Utility functions for RAG Studio that are common across workstreams (e.g., building, deployment, or evaluation).
"""

from databricks.rag.utils.mlflow import (
    update_dataset_version_state,
    get_dataset_version,
)
# https://github.com/databricks/universe/blob/57ed6a9f9021808d361f68ec50669d4d4ce9d56a/model-serving/serving-scheduler/serving-resources/mlflow-serving-server/src/mlflowserving/scoring_server/__init__.py#L378
# TODO(ML-39226): Migrate scoring_server to import databricks.rag.utils.mlflow, then remove this.
from databricks.rag.utils import mlflow as mlflow_utils
from databricks.rag.utils.tables import delimit_qualified_name, get_table_url
from databricks.rag.utils.uc import (
    check_if_catalog_and_schema_exist,
    save_content,
    load_content,
    read_content
)
from databricks.rag.scoring.predictions import RAGCallback


__all__ = [
    "update_dataset_version_state",
    "get_dataset_version",
    "delimit_qualified_name",
    "get_table_url",
    "check_if_catalog_and_schema_exist",
    "save_content",
    "load_content",
    "read_content",
    "RAGCallback",  # TODO (vperiyasamy): we can remove this after the scoring server switches to the new import path.
]
