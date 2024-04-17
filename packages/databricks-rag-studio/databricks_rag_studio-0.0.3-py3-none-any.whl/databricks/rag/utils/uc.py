"""
Helper functions to interact with Unity Catalog.
TODO (vperiyasamy): Move this to a separate package dedicated to Databricks services.
"""

from __future__ import annotations

import databricks.sdk
from databricks.sdk.core import DatabricksError
from databricks.rag import configs
from databricks.rag.entities import UnityCatalogVolume
import os


def check_if_catalog_and_schema_exist(
    extended_config: configs.ExtendedConfig,
) -> None:
    """
    Checks if the schema and catalog exist in the workspace

    :param schema_name: The name of the schema to check
    """
    w = databricks.sdk.WorkspaceClient()
    input_config = extended_config.input_config
    global_config = input_config.global_config
    catalog_name = global_config.uc_assets_location.catalog
    schema_name = f"{catalog_name}.{global_config.uc_assets_location.schema}"
    error_string_check = "does not exist"

    try:
        w.catalogs.get(catalog_name)
    except DatabricksError as e:
        if error_string_check in str(e):
            raise Exception(
                f"The provided catalog {catalog_name} "
                "does not exist. Please check your config"
            )
        raise e

    try:
        w.schemas.get(schema_name)
    except DatabricksError as e:
        if error_string_check in str(e):
            raise Exception(
                f"The provided schema {schema_name} "
                "does not exist. Please check your config"
            )
        raise e


def strip_prefix_from_file(file_path: str, prefix: str) -> str:
    """Strip the UC volume path from the file path."""
    if file_path.startswith(prefix):
        return file_path[len(prefix) :]
    else:
        return file_path


def append_prefix_to_file(file_name: str, prefix: str) -> str:
    """Reconstruct the URL of a document from its file path."""
    return os.path.join(prefix, file_name)


def save_content(
    df: DataFrame,  # noqa: F821
    uc_volume: UnityCatalogVolume,
    url_prefix: str,
    content_column: str,
    source_uri_column: str,
):
    uc_volume_path = uc_volume.path()

    def upload_article(article):
        """Upload article to UC volume."""
        # Strip the prefix from the URL to get the file name
        file_name = strip_prefix_from_file(article[source_uri_column], url_prefix)
        file_path = append_prefix_to_file(file_name, uc_volume_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(article[content_column])

    df.foreach(upload_article)


# This method is replaced by read_content in modern versions of the RAG DAB.
def load_content(
    uc_volume: UnityCatalogVolume,
    url_prefix: str,
    content_column: str,
    source_uri_column: str,
) -> DataFrame:  # noqa: F821
    """
    Load source documents from a UC volume to a Spark DataFrame. Content is decoded from binary to
    string using a UTF-8 decoder.

    :param uc_volume: The UC volume to load documents
    :param url_prefix: Prefix of the source URL
    :param source_uri_column: Column name of the URLs in the result DataFrame.
    :param content_column: Column name of the content in the result DataFrame.
    :return: Spark DataFrame with schema [('doc_uri', 'string'), ('content', 'string')]
    """
    from pyspark.sql.functions import udf

    df = read_content(uc_volume, url_prefix, content_column, source_uri_column).withColumn(
        content_column, udf(lambda x: x.decode("utf-8"))(content_column)
    )
    return df.select(source_uri_column, content_column)


def read_content(
    uc_volume: UnityCatalogVolume,
    url_prefix: str,
    content_column: str,
    source_uri_column: str,
) -> DataFrame:  # noqa: F821
    """
    Load source documents from a UC volume to a Spark DataFrame.

    :param uc_volume: The UC volume to load documents
    :param url_prefix: Prefix of the source URL
    :param source_uri_column: Column name of the URLs in the result DataFrame.
    :param content_column: Column name of the content in the result DataFrame.
    :return: Spark DataFrame with schema [('doc_uri', 'string'), ('content', 'binary')]
    """
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import udf, lit

    spark = SparkSession.getActiveSession()

    # We are assuming that data is stored in UC volumes in binary format.
    # File format can be exposed as a knob in the future.
    raw_df = (
        spark.read.format("binaryFile")
        .option("recursiveFileLookup", "true")
        .load(uc_volume.dbfs_path())
    )

    file_name_column = "__file_name"
    df = raw_df.withColumn(
        file_name_column,
        udf(strip_prefix_from_file)("path", lit(uc_volume.dbfs_path() + "/")),
    ).withColumn(
        source_uri_column,
        udf(append_prefix_to_file)(file_name_column, lit(url_prefix)),
    ).withColumnRenamed("content", content_column)
    return df.select(source_uri_column, content_column)
