from typing import Optional

from delta.tables import DeltaTable
from pyspark.sql import DataFrame, SparkSession, window
from pyspark.sql import functions as F

import databricks.sdk
from databricks.rag.utils import tables


def get_payload_table_name(endpoint_name: str) -> str:
    """
    Return the payload table name for the given endpoint name

    :param endpoint_name: The name of the endpoint
    :return: The fully qualified payload table name
    """
    ws_client = databricks.sdk.WorkspaceClient()
    endpoint_config = ws_client.serving_endpoints.get(endpoint_name).config
    auto_capture_config = endpoint_config.auto_capture_config

    payload_catalog = auto_capture_config.catalog_name
    payload_schema = auto_capture_config.schema_name

    payload_table_name = auto_capture_config.state.payload_table.name
    # TODO ML-38660: Use UnityCatalogTable.full_name() instead
    return tables.delimit_qualified_name(
        f"{payload_catalog}.{payload_schema}.{payload_table_name}"
    )


def dedup_assessment_logs(
    assessment_logs: DataFrame, granularity: Optional[str] = None
) -> DataFrame:
    """
    Deduplicates the given assessment logs DataFrame by only keeping the latest entry matching
    a given request_id and step_id.

    :param assessment_logs: Assessment logs to deduplicate
    :param granularity: Time granularity of the deduplication (e.g., remove all duplicates per "hour").
                        String value here should conform to a format string of pyspark.sql.functions.date_trunc
                        (https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.functions.date_trunc.html).
                        Currently, only "hour" is supported.
                        If None, deduplication is done across the entire dataset.
    :return: Filtered DataFrame of assessment logs
    """
    _ROW_NUM_COL = "row_num"
    _TRUNCATED_TIME_COL = "truncated_time"
    _ASSESSMENT_LOG_PRIMARY_KEYS = [
        F.col("request_id"),
        F.col("step_id"),
        F.col("source.id"),
        # Retrieval assessments are additionally identified by their chunk position.
        F.coalesce(F.col("retrieval_assessment.position"), F.lit(None)),
    ]
    _SUPPORTED_GRANULARITIES = ["hour"]

    if granularity is not None and granularity not in _SUPPORTED_GRANULARITIES:
        raise ValueError(
            f"granularity must be one of {_SUPPORTED_GRANULARITIES} or None, but got {granularity}"
        )

    partition_cols = _ASSESSMENT_LOG_PRIMARY_KEYS + (
        [F.date_trunc(granularity, "timestamp")] if granularity is not None else []
    )
    window_spec = window.Window.partitionBy(partition_cols).orderBy(F.desc("timestamp"))

    # Use row_number() to assign a rank to each row within the window
    assessments_ranked = assessment_logs.withColumn(
        _ROW_NUM_COL, F.row_number().over(window_spec)
    )

    # Filter the rows where row_num is 1 to keep only the latest timestamp
    return assessments_ranked.filter(F.col(_ROW_NUM_COL) == 1).drop(
        _ROW_NUM_COL, _TRUNCATED_TIME_COL
    )


def persist_stream(
    table_name: str, stream_df: DataFrame, checkpoint_location: str
) -> None:
    """
    Writes a streaming DataFrame to a target table location using availableNow semantics
    with checkpointing enabled. If the table does not exist already, initializes it.

    :param table_name: Name of the table
    :param stream_df: Streaming DataFrame to write
    :param checkpoint_location: Checkpoint location to use
    """
    # Initialize the table with CDF enabled if it doesn't exist yet
    spark = SparkSession.getActiveSession()
    (
        DeltaTable.createIfNotExists(spark)
        .tableName(table_name)
        .addColumns(stream_df.schema)
        .property("delta.enableChangeDataFeed", "true")
        .property("delta.columnMapping.mode", "name")
        .execute()
    )

    # Write the stream with the defined checkpoint location
    (
        stream_df.writeStream.format("delta")
        .trigger(availableNow=True)
        .outputMode("append")
        .option("checkpointLocation", checkpoint_location)
        .toTable(table_name)
        .awaitTermination()
    )
