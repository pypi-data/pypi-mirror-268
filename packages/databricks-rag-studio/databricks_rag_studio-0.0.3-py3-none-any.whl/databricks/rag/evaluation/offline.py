import pandas as pd
from pyspark.sql import functions as F, DataFrame, types as T, SparkSession
from delta.tables import DeltaTable

from databricks.rag.unpacking.schemas import (
    CHUNK_SCHEMA,
    TRACE_SCHEMA,
)
from databricks.rag.utils.mlflow import get_model_uri
from databricks.rag.scoring.predictions import RAGCallback


def _invoke_with_chain(rag, chain, messages):
    return rag.invoke(chain, messages)


def generate_offline_predictions(
    eval_dataset: DataFrame, chain, model_name, model_version
) -> DataFrame:
    """
    Generate predictions and traces over an eval_dataset
    """
    rag = RAGCallback()

    @F.pandas_udf("response string, trace string")
    def invoke_udf(messages_series: pd.Series) -> pd.DataFrame:
        responses = []
        traces = []
        for messages in messages_series:
            response, trace = _invoke_with_chain(rag, chain, {"messages": messages})
            # Assume the chain only returns a 1-element choices array
            responses.append(response["choices"][0]["message"]["content"])
            traces.append(trace)

        # Create a DataFrame from the results
        return pd.DataFrame({"response": responses, "trace": traces})

    # Apply the pandas_udf to the DataFrame
    df_with_predictions = eval_dataset.withColumn(
        "raw_predictions", invoke_udf(F.col("request.messages"))
    )

    # Selecting and renaming columns
    df_with_string_outputs = df_with_predictions.selectExpr(
        "*",
        "raw_predictions.response as response_string",
        "raw_predictions.trace as trace_string",
    )

    # Parsing traces and responses, and matching schema
    try:
        app_version_id = get_model_uri(model_name, model_version)
    except ValueError:
        app_version_id = ""
    return (
        df_with_string_outputs.withColumn(
            "trace",
            F.from_json("trace_string", TRACE_SCHEMA).withField(
                "app_version_id", F.lit(app_version_id)
            ),
        )
        .withColumn(
            "output",
            F.struct(
                F.array(
                    F.struct(
                        F.struct(
                            F.lit("assistant").alias("role"),
                            F.col("response_string").alias("content"),
                        ).alias("message")
                    )
                ).alias("choices")
            ),
        )
        .select("request", "trace", "output", "ground_truth")
    )


def add_labels_to_eval_dataset(
    flat_ground_truth_data: DataFrame,
    eval_table_name: str,
):
    """
    Add labels from a flat table to an eval table and update using delta merge

    :param flat_ground_truth_data: The flat table containing the labels to add to the eval table. The flat table must have an id column of type StringType, an answer column of type StringType, and a doc_ids column of type StringType.
    :param eval_table_name: The eval table must follow the eval table input schema.
    """
    spark = SparkSession.getActiveSession()

    # Check that "id", "answer", and "doc_ids" columns exist in the flat table and are of StringType
    flat_table_schema = flat_ground_truth_data.schema
    required_columns = ["id", "answer", "doc_ids"]
    for column in required_columns:
        if column not in flat_table_schema.names:
            raise ValueError(f"Column {column} is required in the flat table.")

        column_type = flat_table_schema[column].dataType
        if not isinstance(column_type, T.StringType):
            raise ValueError(f"Column {column} must be of type StringType.")

    # Split the doc_ids column into an array of strings
    doc_ids_not_empty = F.length(F.trim(flat_ground_truth_data["doc_ids"])) > 0
    split_doc_ids = F.when(
        doc_ids_not_empty, F.split(flat_ground_truth_data["doc_ids"], ",")
    ).otherwise(F.array())

    # Use F.transform to create an array of structures for each document ID
    doc_structs = F.transform(
        split_doc_ids,
        lambda doc_id: F.struct(
            *[
                F.lit(None).cast(field.dataType).alias(field.name)
                for field in CHUNK_SCHEMA.fields
            ]
        ).withField("doc_uri", doc_id),
    )

    # Create the ground truth struct
    # NOTE: we should not change schema of the ground_truth column without a plan to handle schema evolution in the delta merge
    flat_ground_truth_data_with_ground_truth_struct = flat_ground_truth_data.withColumn(
        "ground_truth",
        F.struct(
            F.struct(F.col("answer").alias("content")).alias("text_output"),
            F.struct(
                F.lit(None).cast(T.StringType()).alias("name"),
                doc_structs.alias("chunks"),
            ).alias("retrieval_output"),
        ),
    )

    eval_table_delta = DeltaTable.forName(spark, eval_table_name)

    # Use delta merge to update the eval_table with the ground_truth for rows where the flat_ground_truth_data_with_ground_truth_struct id matches the eval_table request.request_id
    eval_table_delta.alias("eval_table").merge(
        flat_ground_truth_data_with_ground_truth_struct.alias("flat_table"),
        F.col("eval_table.request.request_id") == F.col("flat_table.id"),
    ).whenMatchedUpdate(
        set={
            "eval_table.ground_truth": F.col("flat_table.ground_truth"),
        }
    ).execute()
