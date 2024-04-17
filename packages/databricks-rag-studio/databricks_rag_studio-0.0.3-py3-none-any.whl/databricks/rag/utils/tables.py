from mlflow.utils.annotations import deprecated

from databricks.rag.entities import UnityCatalogTable


@deprecated("Use UnityCatalogTable.full_name() instead.")
def delimit_qualified_name(qualified_name: str) -> str:
    """
    Delimits the given qualified table name with backticks
    so that we can handle special characters (like hyphens) in queries.
    For example, "a.b.c" becomes "`a`.`b`.`c`".

    :param qualified_name: The qualified name to delimit
    :return: The delimited qualified name
    """
    return UnityCatalogTable.from_full_name(qualified_name).full_name()


@deprecated("Use UnityCatalogTable.get_table_url_in_workspace() instead.")
def get_table_url(workspace_url: str, qualified_table_name: str) -> str:
    """
    Get the URL for the given table in the provided workspace.
    :param workspace_url: URL of the workspace to link to
    :param qualified_table_name: Fully qualified name of the table, e.g., "catalog.schema.table".
    :return: URL of the table in the Catalog Explorer
    """
    return UnityCatalogTable.from_full_name(
        qualified_table_name
    ).get_table_url_in_workspace(workspace_url)
