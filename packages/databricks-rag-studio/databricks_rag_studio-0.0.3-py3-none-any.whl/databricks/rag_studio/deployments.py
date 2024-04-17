from typing import List, Optional
import uuid

# SDK for rag
from mlflow import set_registry_uri
from mlflow.utils import databricks_utils
from databricks.rag_studio.sdk_utils.permissions_checker import (
    _check_view_permissions_on_deployment,
)
from databricks.rag_studio.feedback import _FEEDBACK_MODEL_NAME, log_feedback_model
from databricks.rag_studio.sdk_utils.entities import Deployment
from databricks.rag_studio.sdk_utils.deployments import _get_deployments
from databricks.rag_studio.client.rest_client import (
    deploy_chain as rest_deploy_chain,
    list_chain_deployments as rest_list_chain_deployments,
)
from databricks.rag_studio.utils.mlflow_utils import _get_latest_model_version
from databricks.rag_studio.utils.uc import (
    _remove_dots,
    _get_catalog_and_schema,
    _check_model_name,
)
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.serving import (
    EndpointCoreConfigInput,
    EndpointCoreConfigOutput,
    ServedModelInput,
    TrafficConfig,
    Route,
    AutoCaptureConfigInput,
    ServedModelInputWorkloadSize,
    EndpointPendingConfig,
)
from databricks.sdk.errors.platform import (
    ResourceDoesNotExist,
    ResourceConflict,
    InvalidParameterValue,
    BadRequest,
)


def get_deployments(
    model_name: str, model_version: Optional[int] = None
) -> List[Deployment]:
    """
    Get chain deployments metadata.

    :param model_name: Name of the UC registered model
    :param model_version: (Optional) Version numbers for specific chains.
    :return: All deployments for the UC registered model.
    """
    return _get_deployments(model_name, model_version)


def _create_served_model_input(model_name, version, model_input_name, scale_to_zero):
    return ServedModelInput(
        name=_remove_dots(model_input_name),
        model_name=model_name,
        model_version=version,
        workload_size=ServedModelInputWorkloadSize.SMALL,
        scale_to_zero_enabled=scale_to_zero,
    )


def _create_endpoint_name(model_name):
    full_name = f"rag_studio_{_remove_dots(model_name)}"
    return full_name[:60]


def _create_served_model_name(model_name, version):
    full_name = f"{_remove_dots(model_name)}_{version}"
    return full_name[:60]


def _create_feedback_model_name(model_name: str) -> str:
    catalog_name, schema_name = _get_catalog_and_schema(model_name)
    return f"{catalog_name}.{schema_name}.{_FEEDBACK_MODEL_NAME}"


def _create_feedback_model(
    feedback_uc_model_name: str, scale_to_zero: bool
) -> ServedModelInput:
    set_registry_uri("databricks-uc")

    # only create the feedback model if it doesn't already exist in this catalog.schema
    feedback_model_version = str(_get_latest_model_version(feedback_uc_model_name))
    if feedback_model_version == "0":
        # also adds to UC with version '1'
        log_feedback_model(feedback_uc_model_name)
        feedback_model_version = str(_get_latest_model_version(feedback_uc_model_name))
    return _create_served_model_input(
        feedback_uc_model_name,
        feedback_model_version,
        _FEEDBACK_MODEL_NAME,
        scale_to_zero,
    )


def _parse_pending_config_for_feedback_config(
    uc_model_name: str, pending_config: EndpointPendingConfig
) -> EndpointCoreConfigOutput:
    """
    Parse pending_config to get additional information about the feedback model in order to
    return a config as if the endpoint was successfully deployed with only the feedback model.
    This way we can reuse the update functions that are written for normal endpoint updates.
    """
    feedback_uc_model_name = _create_feedback_model_name(uc_model_name)
    for model in pending_config.served_models:
        if model.name == _FEEDBACK_MODEL_NAME:
            feedback_model_version = model.model_version
            scale_to_zero = model.scale_to_zero_enabled

    return EndpointCoreConfigOutput(
        served_models=[
            _create_served_model_input(
                model_name=feedback_uc_model_name,
                version=feedback_model_version,
                model_input_name=_FEEDBACK_MODEL_NAME,
                scale_to_zero=scale_to_zero,
            )
        ],
        traffic_config=TrafficConfig(
            routes=[Route(served_model_name=_FEEDBACK_MODEL_NAME, traffic_percentage=0)]
        ),
        auto_capture_config=pending_config.auto_capture_config,
    )


def _construct_table_name(catalog_name, schema_name, model_name):
    w = WorkspaceClient()
    # remove catalog and schema from model_name and add rag_studio- prefix
    base_name = "rag_studio-" + model_name.split(".")[2]
    suffix = ""

    # try to append suffix
    for index in range(20):
        if index != 0:
            suffix = f"_{index}"

        table_name = f"{base_name[:63-len(suffix)]}{suffix}"

        full_name = f"{catalog_name}.{schema_name}.{table_name}_payload"
        if not w.tables.exists(full_name=full_name).table_exists:
            return table_name

    # last attempt - append uuid and truncate to 63 characters (max length for table_name_prefix)
    # unlikely to have conflict unless base_name is long
    if len(base_name) > 59:
        return f"{base_name[:59]}_{uuid.uuid4().hex}"[:63]
    return f"{base_name}_{uuid.uuid4().hex}"[:63]


def _create_new_endpoint_config(
    model_name, version, endpoint_name, scale_to_zero=False
):
    catalog_name, schema_name = _get_catalog_and_schema(model_name)

    served_model_name = _create_served_model_name(model_name, version)
    feedback_uc_model_name = _create_feedback_model_name(model_name)

    table_name = _construct_table_name(catalog_name, schema_name, model_name)

    return EndpointCoreConfigInput(
        name=endpoint_name,
        served_models=[
            _create_served_model_input(
                model_name, version, served_model_name, scale_to_zero
            ),
            _create_feedback_model(feedback_uc_model_name, scale_to_zero),
        ],
        traffic_config=TrafficConfig(
            routes=[
                Route(
                    served_model_name=served_model_name,
                    traffic_percentage=100,
                ),
                Route(
                    served_model_name=_FEEDBACK_MODEL_NAME,
                    traffic_percentage=0,
                ),
            ]
        ),
        auto_capture_config=AutoCaptureConfigInput(
            catalog_name=catalog_name,
            schema_name=schema_name,
            table_name_prefix=table_name,
        ),
    )


def _update_traffic_config(
    model_name: str,
    version: str,
    existing_config: EndpointCoreConfigOutput,
) -> TrafficConfig:
    served_model_name = _create_served_model_name(model_name, version)
    updated_routes = [
        Route(served_model_name=served_model_name, traffic_percentage=100)
    ]

    if existing_config:
        for traffic_config in existing_config.traffic_config.routes:
            updated_routes.append(
                Route(
                    served_model_name=traffic_config.served_model_name,
                    traffic_percentage=0,
                )
            )
    return TrafficConfig(routes=updated_routes)


def _update_served_models(
    model_name: str,
    version: str,
    endpoint_name: str,
    existing_config: EndpointCoreConfigOutput,
    scale_to_zero: bool,
) -> List[ServedModelInput]:
    served_model_name = _create_served_model_name(model_name, version)
    updated_served_models = [
        _create_served_model_input(
            model_name, version, served_model_name, scale_to_zero
        )
    ]

    if existing_config:
        updated_served_models.extend(existing_config.served_models)

    return updated_served_models


def _construct_query_endpoint(workspace_url, endpoint_name, model_name, version):
    # This is a temporary solution until we can identify the appropriate solution to get
    # the workspace URI in backend. Ref: https://databricks.atlassian.net/browse/ML-39391
    served_model_name = _create_served_model_name(model_name, version)
    return f"{workspace_url}/serving-endpoints/{endpoint_name}/served-models/{served_model_name}/invocations"


def deploy_model(model_name: str, version: int, **kwargs) -> Deployment:
    """
    Deploy new version of the RAG chain.

    :param model_name: Name of UC registered model
    :param version: Model version #

    :return: Chain deployment metadata.
    """
    _check_model_name(model_name)
    endpoint_name = _create_endpoint_name(model_name)
    w = WorkspaceClient()
    scale_to_zero = kwargs.get("scale_to_zero", False)
    try:
        endpoint = w.serving_endpoints.get(endpoint_name)
    except ResourceDoesNotExist:
        w.serving_endpoints.create(
            name=endpoint_name,
            config=_create_new_endpoint_config(
                model_name, version, endpoint_name, scale_to_zero
            ),
        )
    else:
        config = endpoint.config
        # TODO: https://databricks.atlassian.net/browse/ML-39649
        # config=None means this endpoint has never successfully deployed before
        # bc we have a dummy feedback model, we know feedback works, so we only want its config
        if config is None:
            config = _parse_pending_config_for_feedback_config(
                model_name, endpoint.pending_config
            )

        # ignore pending_config bc we only redeploy models that have succesfully deployed before
        # set the traffic config for all currently deployed models to be 0
        updated_traffic_config = _update_traffic_config(model_name, version, config)
        updated_served_models = _update_served_models(
            model_name, version, endpoint_name, config, scale_to_zero
        )
        try:
            w.serving_endpoints.update_config(
                name=endpoint_name,
                served_models=updated_served_models,
                traffic_config=updated_traffic_config,
                auto_capture_config=config.auto_capture_config,
            )
        except ResourceConflict:
            raise ValueError("The endpoint is currently updating")
        except InvalidParameterValue as e:
            if "served_models cannot contain more than 15 elements" in str(e):
                raise ValueError(
                    "There are already 15 models deployed to this endpoint. Please delete one before deploying."
                )
            else:
                # pass through any other errors
                raise e
        except BadRequest as e:
            if "Cannot create 2+ served entities" in str(e):
                raise ValueError(
                    """You cannot redeploy the same model and version more than once.
Update the version number"""
                )
            else:
                raise e

    workspace_url = f"https://{databricks_utils.get_browser_hostname()}"
    return rest_deploy_chain(
        model_name=model_name,
        model_version=version,
        query_endpoint=_construct_query_endpoint(
            workspace_url, endpoint_name, model_name, version
        ),
        endpoint_name=endpoint_name,
        served_entity_name=_create_served_model_name(model_name, version),
        workspace_url=workspace_url,
    )


def list_deployments() -> List[Deployment]:
    """
    :return: List of all RAG chain deployments
    """
    deployments = rest_list_chain_deployments()
    deployments_with_permissions = []
    for deployment in deployments:
        try:
            _check_view_permissions_on_deployment(deployment)
            deployments_with_permissions.append(deployment)
        except ValueError:
            pass
        except ResourceDoesNotExist:
            pass
    return deployments_with_permissions
