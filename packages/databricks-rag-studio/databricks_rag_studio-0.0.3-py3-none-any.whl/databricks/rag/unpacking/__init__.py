import os
from typing import Tuple

from databricks.rag.unpacking.schemas import (
    ASSESSMENT_PROTO_SCHEMA,
    CHOICES_SCHEMA,
    MESSAGES_SCHEMA,
    MLFLOW_TRACE_SCHEMA_VERSION,
    RETRIEVAL_ASSESSMENT_TABLE_SCHEMA,
    TEXT_ASSESSMENT_TABLE_SCHEMA,
    TRACE_SCHEMA,
    TRACE_V2_SCHEMA,
)
from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql import types as T


def _rag_trace_v2_enabled():
    return os.environ.get("RAG_TRACE_V2_ENABLED", "false").lower() == "true"


def _generate_request_logs_old(df: DataFrame) -> DataFrame:
    request_payloads = df.filter(
        F.expr(
            f"response:databricks_output.trace['{MLFLOW_TRACE_SCHEMA_VERSION}'] IS NULL"
        )
    )
    return (
        request_payloads.withColumn(
            "request",
            F.struct(
                F.col("databricks_request_id").alias("request_id"),
                F.expr("request:databricks_options.conversation_id").alias(
                    "conversation_id"
                ),
                F.col("timestamp"),
                F.from_json(F.expr("request:messages"), MESSAGES_SCHEMA).alias(
                    "messages"
                ),
                F.element_at(
                    F.from_json(F.expr("request:messages"), MESSAGES_SCHEMA), -1
                )
                .getItem("content")
                .alias("last_input"),
            ),
        )
        .withColumn(
            "trace",
            F.from_json(F.expr("response:databricks_output.trace"), TRACE_SCHEMA),
        )
        .withColumn(
            "output",
            F.struct(
                F.from_json(F.expr("response:choices"), CHOICES_SCHEMA).alias("choices")
            ),
        )
        .select("request", "trace", "output")
    )


def _generate_request_logs_v2(df: DataFrame) -> DataFrame:
    return (
        df.withColumn(
            "request",
            F.struct(
                F.col("databricks_request_id").alias("request_id"),
                F.expr("request:databricks_options.conversation_id").alias(
                    "conversation_id"
                ),
                F.col("timestamp"),
                F.from_json(F.expr("request:messages"), MESSAGES_SCHEMA).alias(
                    "messages"
                ),
                F.element_at(
                    F.from_json(F.expr("request:messages"), MESSAGES_SCHEMA), -1
                )
                .getItem("content")
                .alias("last_input"),
            ),
        )
        .withColumn(
            "trace",
            F.from_json(F.expr("response:databricks_output.trace"), TRACE_V2_SCHEMA),
        )
        .withColumn(
            "output",
            F.struct(
                F.from_json(F.expr("response:choices"), CHOICES_SCHEMA).alias("choices")
            ),
        )
        .select("request", "trace", "output")
    )


def _generate_assessment_logs(payload_df: DataFrame) -> DataFrame:
    assessment_payloads = payload_df.filter(F.expr("response:choices IS NULL"))
    assessment_logs = (
        assessment_payloads.withColumn(
            "assessments",
            F.explode(
                F.from_json(
                    F.expr("request:dataframe_records"), ASSESSMENT_PROTO_SCHEMA
                )
            ),
        )
        .withColumn(
            "text_assessments",
            # Transform the list of text assessments into a list of assessment structs (with empty
            # retrieval assessments) so we can concatenate them before exploding.
            # The ordering of the structs must match exactly to concatenate them.
            F.transform(
                F.col("assessments.text_assessments"),
                lambda ta: F.struct(
                    # Transform the proto ratings map (which only has a boolean value)
                    # to the table ratings map (which has bool_value and double_value).
                    F.struct(
                        ta.step_id,
                        F.transform_values(
                            ta.ratings,
                            lambda _, rating_val: F.struct(
                                rating_val.value.alias("bool_value"),
                                F.lit(None).cast(T.DoubleType()).alias("double_value"),
                                rating_val.rationale,
                            ),
                        ).alias("ratings"),
                        ta.free_text_comment,
                        ta.suggested_output,
                    ).alias("text_assessment"),
                    F.lit(None)
                    .cast(RETRIEVAL_ASSESSMENT_TABLE_SCHEMA)
                    .alias("retrieval_assessment"),
                ),
            ),
        )
        .withColumn(
            "retrieval_assessments",
            # Transform the list of retrieval assessments into a list of assessment structs (with empty
            # text assessments) so we can concatenate them before exploding.
            # The ordering of the structs must match exactly to concatenate them.
            F.transform(
                F.col("assessments.retrieval_assessments"),
                lambda ra: F.struct(
                    F.lit(None)
                    .cast(TEXT_ASSESSMENT_TABLE_SCHEMA)
                    .alias("text_assessment"),
                    # Transform the proto ratings map (which only has a boolean value)
                    # to the table ratings map (which has bool_value and double_value).
                    F.struct(
                        ra.position,
                        ra.step_id,
                        F.transform_values(
                            ra.ratings,
                            lambda _, rating_val: F.struct(
                                rating_val.value.alias("bool_value"),
                                F.lit(None).cast(T.DoubleType()).alias("double_value"),
                                rating_val.rationale,
                            ),
                        ).alias("ratings"),
                        ra.free_text_comment,
                    ).alias("retrieval_assessment"),
                ),
            ),
        )
        .withColumn(
            "all_assessments",
            F.explode(
                F.concat(
                    # Coalesce with an empty array to handle cases where only one of
                    # text_assessments or retrieval_assessments were passed.
                    F.coalesce(F.col("text_assessments"), F.array()),
                    F.coalesce(F.col("retrieval_assessments"), F.array()),
                )
            ),
        )
        .select(
            "assessments.request_id",
            F.coalesce(
                F.col("all_assessments.text_assessment.step_id"),
                F.col("all_assessments.retrieval_assessment.step_id"),
            ).alias("step_id"),
            "assessments.source",
            "timestamp",
            "all_assessments.text_assessment",
            "all_assessments.retrieval_assessment",
        )
    )
    return assessment_logs


def _generate_request_logs(payload_df: DataFrame) -> DataFrame:
    request_payloads = payload_df.filter(F.expr("response:choices IS NOT NULL"))
    request_payloads_v2 = request_payloads.filter(
        F.expr(f"response:databricks_output.trace['{MLFLOW_TRACE_SCHEMA_VERSION}']==2")
    )

    if _rag_trace_v2_enabled() and not request_payloads_v2.isEmpty():
        return _generate_request_logs_v2(request_payloads_v2)

    return _generate_request_logs_old(request_payloads)


def unpack_and_split_payloads(payload_df: DataFrame) -> Tuple[DataFrame, DataFrame]:
    """
    Unpacks the request and assessment payloads from the given DataFrame
    and splits them into separate request log and assessment log DataFrames.
    :param payload_df: A DataFrame containing payloads to unpack and split
    :return: A tuple containing (request logs DataFrame, assessment logs DataFrame)
    """
    payloads = payload_df.filter(
        F.col("status_code") == "200"
    ).withColumn(  # Ignore error requests
        "timestamp", (F.col("timestamp_ms") / 1000).cast("timestamp")
    )

    # Split the payloads into requests and assessments based on the payload structure
    request_logs = _generate_request_logs(payloads)
    assessment_logs = _generate_assessment_logs(payloads)

    return request_logs, assessment_logs
