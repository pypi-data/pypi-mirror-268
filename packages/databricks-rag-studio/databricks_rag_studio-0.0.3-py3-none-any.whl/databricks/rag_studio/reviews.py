from typing import List, Optional
import mlflow
from databricks.rag_studio.sdk_utils.permissions_checker import (
    _check_manage_permissions_on_deployment,
)
from databricks.rag_studio.client.rest_client import (
    get_chain_deployments as rest_get_chain_deployments,
    create_review_artifacts as rest_create_review_artifacts,
)
from databricks.sdk import WorkspaceClient

_TRACES_FILE_PATH = "traces.json"


def _convert_inference_table_to_tracing_schema(request_payloads):
    """
    Convert the inference table to the schema required for tracing
    """
    from pyspark.sql import functions as F
    from databricks.rag_studio.sdk_utils.schemas import (
        MESSAGES_SCHEMA,
        CHOICES_SCHEMA,
        TRACE_SCHEMA,
    )

    changed_request_payloads = request_payloads.filter(
        F.expr("response:choices IS NOT NULL")
    ).withColumn(  # Ignore error requests
        "timestamp", (F.col("timestamp_ms") / 1000).cast("timestamp")
    )

    return (
        changed_request_payloads.withColumn(
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


def _get_table_name(auto_capture_config):
    catalog_name = auto_capture_config.catalog_name
    schema_name = auto_capture_config.schema_name
    table_name = auto_capture_config.state.payload_table.name
    return f"`{catalog_name}`.`{schema_name}`.`{table_name}`"


def _get_inference_table_from_serving(model_name, serving_endpoint_name):
    w = WorkspaceClient()
    serving_endpoint = w.serving_endpoints.get(serving_endpoint_name)
    if (
        serving_endpoint.config is None
        or serving_endpoint.config.auto_capture_config is None
    ):
        raise ValueError(
            f"The provided {model_name} doesn't have any inference table configured. "
            "Please update the endpoint to capture payloads to an inference table"
        )

    auto_capture_config = serving_endpoint.config.auto_capture_config
    if (
        auto_capture_config.catalog_name is None
        or auto_capture_config.schema_name is None
    ):
        raise ValueError(
            f"The provided {model_name} doesn't have any inference table configured. "
            "Please update the endpoint to capture payloads to an inference table"
        )

    return _get_table_name(auto_capture_config)


def enable_trace_reviews(
    model_name: str, request_ids: Optional[List[str]] = None
) -> str:
    """
    Enable the reviewer UI to collect feedback on the conversations from the endpoint inference log.

    :param model_name: The name of the UC Registered Model to use when
                registering the chain as a UC Model Version.
                Example: catalog.schema.model_name
    :param request_ids: Optional list of request_ids for which the feedback
                needs to be captured. Example: ["490cf09b-6da6-474f-bc35-ee5ca688ff8d",
                "a4d37810-5cd0-4cbd-aa25-e5ceaf6a448b"]

    :return: URL for the reviewer UI where users can start providing feedback

    Example:
    ```
    from databricks.rag_studio import enable_trace_reviews

    enable_trace_reviews(
        model_name="catalog.schema.chain_model",
        request_ids=["490cf09b-6da6-474f-bc35-ee5ca688ff8", "a4d37810-5cd0-4cbd-aa25-e5ceaf6a448"],
    )
    ```
    """
    chain_deployments = rest_get_chain_deployments(model_name)
    _ = [
        _check_manage_permissions_on_deployment(deployment)
        for deployment in chain_deployments
    ]

    if len(chain_deployments) == 0:
        raise ValueError(
            f"The provided {model_name} has never been deployed. "
            "Please deploy the model first using deploy_chain API"
        )
    chain_deployment = chain_deployments[-1]
    serving_endpoint_name = chain_deployment.endpoint_name
    table_full_name = _get_inference_table_from_serving(
        model_name, serving_endpoint_name
    )

    if request_ids:
        # cast id to int if other type is passed in
        request_ids_str = ", ".join([f"'{id}'" for id in request_ids])
        sql_query = f"SELECT * FROM {table_full_name} WHERE databricks_request_id IN ({request_ids_str})"
    else:
        sql_query = f"SELECT * FROM {table_full_name}"

    from pyspark.sql import SparkSession

    spark = SparkSession.builder.getOrCreate()
    try:
        spark_df = spark.sql(sql_query)
        converted_spark_df = _convert_inference_table_to_tracing_schema(spark_df)
        df = converted_spark_df.toPandas()
    except Exception as e:
        raise ValueError(
            f"Failed to fetch the data from the table {table_full_name}. Error: {str(e)}"
        ) from e

    with mlflow.start_run() as model_run:
        mlflow.log_table(data=df, artifact_file=_TRACES_FILE_PATH)
        artifact_uri = f"runs:/{model_run.info.run_id}/{_TRACES_FILE_PATH}"
        rest_create_review_artifacts(model_name, artifacts=[artifact_uri])

    return chain_deployment.rag_app_url
