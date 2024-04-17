"""Functionality for online and offline evaluation of RAG chains."""

from databricks.rag.evaluation.offline import (
    add_labels_to_eval_dataset,
    generate_offline_predictions,
)
from databricks.rag.evaluation.online import (
    get_payload_table_name,
    dedup_assessment_logs,
    persist_stream,
)

__all__ = [
    "add_labels_to_eval_dataset",
    "generate_offline_predictions",
    "get_payload_table_name",
    "dedup_assessment_logs",
    "persist_stream",
]
