import mlflow
from mlflow import MlflowClient


# TODO: use `get_register_model` when `latest_versions` is fixed for UC models
def _get_latest_model_version(model_name: str) -> int:
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
