import re

from typing import List, Optional, Tuple
from databricks.rag_studio.sdk_utils.entities import PermissionLevel
from databricks.rag_studio.sdk_utils.deployments import _get_deployments
from databricks.rag_studio.client.rest_client import (
    get_review_artifacts as rest_get_review_artifacts,
)
from databricks.sdk import WorkspaceClient
from databricks.sdk.errors.platform import (
    ResourceDoesNotExist,
    Unauthenticated,
    NotFound,
    PermissionDenied,
)
from databricks.sdk.service.serving import (
    ServingEndpointAccessControlRequest,
    ServingEndpointPermissionLevel,
    ServingEndpointPermissions,
)
from databricks.sdk.service.workspace import (
    WorkspaceObjectPermissionLevel,
    WorkspaceObjectPermissions,
    WorkspaceObjectAccessControlRequest,
)


def _get_run_ids_from_artifact_uris(artifact_uris: List[str]) -> List[str]:
    return [
        re.search(r"runs:/(.*?)/.*", artifact_id).group(1)
        for artifact_id in artifact_uris
    ]


def _get_experiment_ids(run_ids: List[str]) -> List[str]:
    w = WorkspaceClient()
    experiment_ids = set()
    for run_id in run_ids:
        run_response = w.experiments.get_run(run_id)
        experiment_ids.add(run_response.run.info.experiment_id)
    return list(experiment_ids)


# Given an endpoint, calls it with the appropriate arguments and handles errors
def _call_workspace_api(endpoint, kwargs):
    try:
        return endpoint(**kwargs)
    except Unauthenticated as e:
        raise ValueError(
            "Unable to authenticate to the databricks workspace: " + str(e)
        ) from e
    except PermissionDenied as e:
        raise ValueError(
            "Permission Denied: User does not have valid permissions for setting permssions on the deployment."
        ) from e
    except ResourceDoesNotExist as e:
        raise ValueError(
            "Resource does not exist, please check your inputs: " + str(e)
        ) from e
    except NotFound as e:
        raise ValueError(
            "Invalid Inputs: Passed in parameters are not found. " + str(e)
        ) from e
    except Exception as e:
        raise e


# Get permissions on a given endpoint
def _get_permissions_on_endpoint(endpoint_id: str) -> ServingEndpointPermissions:
    w = WorkspaceClient()
    permissions = _call_workspace_api(
        w.serving_endpoints.get_permissions, {"serving_endpoint_id": endpoint_id}
    )
    return permissions


# Get permissions on a given experiment
# TODO: Handle a normal experiment as well (ML-39642)
def _get_permissions_on_experiment(experiment_id: str) -> WorkspaceObjectPermissions:
    w = WorkspaceClient()
    permissions = _call_workspace_api(
        w.workspace.get_permissions,
        {"workspace_object_type": "notebooks", "workspace_object_id": experiment_id},
    )
    return permissions


# Given a Permissions Object, and a list of users returns new permissions without the users
def _remove_users_from_permissions_list(permissions, users):
    user_set = set(users)
    acls = permissions.access_control_list
    modified_acls = list(filter(lambda acl: acl.user_name not in user_set, acls))
    # No Changes as the user has no permissions on the endpoint
    if len(modified_acls) == len(acls):
        return None
    new_permissions = []
    for acl in modified_acls:
        for permission in acl.all_permissions:
            user = ()
            # "user_name", "group_name" and "service_principal_name" are all keywords used by the permission API later
            if acl.user_name is not None:
                user = ("user_name", acl.user_name)
            elif acl.group_name is not None:
                user = ("group_name", acl.group_name)
            else:
                user = ("service_principal_name", acl.service_principal_name)
            new_permissions.append((user, permission.permission_level))
    return new_permissions


# For a given a chain model name get all logged trace artifacts and return the corresponding experiment IDs
def _get_experiment_ids_from_trace_artifacts(model_name: str) -> List[str]:
    ml_artifacts = rest_get_review_artifacts(model_name)
    experiment_ids = _get_experiment_ids(
        _get_run_ids_from_artifact_uris(ml_artifacts.artifact_uris)
    )
    return experiment_ids


# Sets permissions on an endoint for the list of users
# Permissions is of type [((User_type, username), PermissionLevel)]
def _set_permissions_on_endpoint(
    endpoint_id: str,
    permissions: List[Tuple[Tuple[str, str], ServingEndpointPermissionLevel]],
):
    if permissions is None:
        return
    acls = []
    for users, permission_level in permissions:
        user_type, user = users
        acls.append(
            ServingEndpointAccessControlRequest.from_dict(
                {user_type: user, "permission_level": permission_level.value}
            )
        )
    # NOTE: THIS SHOULD ONLY BE CALLED ONCE
    # This endpoint performs a complete overwrite and should not be called more than once
    w = WorkspaceClient()
    _call_workspace_api(
        w.serving_endpoints.set_permissions,
        {
            "serving_endpoint_id": endpoint_id,
            "access_control_list": acls,
        },
    )


# Sets permission on experiment
# Permissions is of type [((User_type, username), PermissionLevel)]
def _set_permissions_on_experiment(
    experiment_id: str,
    permissions: List[Tuple[Tuple[str, str], ServingEndpointPermissionLevel]],
):
    if permissions is None:
        return
    acls = []
    for users, permission_level in permissions:
        user_type, user = users
        acls.append(
            WorkspaceObjectAccessControlRequest.from_dict(
                {user_type: user, "permission_level": permission_level.value}
            )
        )
    # NOTE: THIS SHOULD ONLY BE CALLED ONCE
    # This endpoint performs a complete overwrite and should not be called more than once
    w = WorkspaceClient()
    _call_workspace_api(
        w.workspace.set_permissions,
        {
            "workspace_object_type": "notebooks",
            "workspace_object_id": experiment_id,
            "access_control_list": acls,
        },
    )


# Update Permissions on Endpoint
def _update_permissions_on_endpoint(
    endpoint_id: str,
    users: List[str],
    permission_level: ServingEndpointPermissionLevel,
):
    w = WorkspaceClient()
    _call_workspace_api(
        w.serving_endpoints.update_permissions,
        {
            "serving_endpoint_id": endpoint_id,
            "access_control_list": [
                ServingEndpointAccessControlRequest(
                    user_name=user, permission_level=permission_level
                )
                for user in users
            ],
        },
    )


# Update Permissions on Experiment
def _update_permissions_on_experiment(
    experiment_ids: str,
    users: List[str],
    permission_level: Optional[WorkspaceObjectPermissionLevel] = None,
):
    w = WorkspaceClient()
    for experiment_id in experiment_ids:
        _call_workspace_api(
            w.workspace.update_permissions,
            {
                "workspace_object_type": "notebooks",
                "workspace_object_id": experiment_id,
                "access_control_list": [
                    WorkspaceObjectAccessControlRequest(
                        user_name=user,
                        permission_level=permission_level,
                    )
                    for user in users
                ],
            },
        )


def _get_endpoint_id_for_deployed_model(model_name: str):
    endpoint_ids = set()
    chain_deployments = _get_deployments(model_name)
    w = WorkspaceClient()
    for deployment in chain_deployments:
        serving_endpoint = _call_workspace_api(
            w.serving_endpoints.get, {"name": deployment.endpoint_name}
        )
        endpoint_ids.add(serving_endpoint.id)
    return endpoint_ids


def _clear_permissions_for_user_endpoint(endpoint_id: str, clear_users: List[str]):
    # Retrieves all the permissions in the endpoint. Returned list is permission level mapping for all users
    permissions = _get_permissions_on_endpoint(endpoint_id)
    # Filter permissions list such that users in `clear_users` do not have any permissions.
    new_permissions = _remove_users_from_permissions_list(permissions, clear_users)
    # Re sets the permissions for the remaining users
    _set_permissions_on_endpoint(endpoint_id, new_permissions)


def _clear_permissions_for_user_experiments(
    experiment_ids: List[str], clear_users: List[str]
):
    for experiment_id in experiment_ids:
        # Retrieves all the permissions in the experiment. Returned list is permission level mapping for all users
        experiment_permissions = _get_permissions_on_experiment(experiment_id)
        # Filter permissions list such that users in `clear_users` do not have any permissions.
        new_permissions = _remove_users_from_permissions_list(
            experiment_permissions, clear_users
        )
        # Re sets the permisssions for the remaining users
        _set_permissions_on_experiment(experiment_id, new_permissions)


def set_permissions(
    model_name: str,
    users: List[str],
    permission_level: PermissionLevel,
):
    """
    Set permissions to use chat and review apps.

    :param model_name: Name of the UC registered model.
    :param users: List of account users.
    :param permission_level: Permissions level assigned to the list of users. Supported permission levels are
                             `NO_PERMISSIONS`: chat and review privileges revoked for users
                             `CAN_VIEW`: users can list and get metadata for deployed chains
                             `CAN_QUERY`: users can use chat with the RAG chain and provide feedback on their own chats
                             `CAN_REVIEW`: users can provide feedback on review traces
                             `CAN_MANAGE`: users can update existing RAG chain deployments and deploy chains.
    """
    users_set = set(users)
    users = list(users_set)
    endpoint_ids = _get_endpoint_id_for_deployed_model(model_name)

    if len(endpoint_ids) == 0:
        raise ValueError("No deployments found for model_name " + model_name)
    # Set Permissions on Endpoints
    for endpoint_id in endpoint_ids:
        if permission_level == PermissionLevel.NO_PERMISSIONS:
            _clear_permissions_for_user_endpoint(endpoint_id, users)
        elif permission_level == PermissionLevel.CAN_VIEW:
            _update_permissions_on_endpoint(
                endpoint_id, users, ServingEndpointPermissionLevel.CAN_VIEW
            )
        elif permission_level == PermissionLevel.CAN_QUERY:
            _update_permissions_on_endpoint(
                endpoint_id, users, ServingEndpointPermissionLevel.CAN_QUERY
            )
        elif permission_level == PermissionLevel.CAN_REVIEW:
            _update_permissions_on_endpoint(
                endpoint_id, users, ServingEndpointPermissionLevel.CAN_QUERY
            )
        elif permission_level == PermissionLevel.CAN_MANAGE:
            _update_permissions_on_endpoint(
                endpoint_id, users, ServingEndpointPermissionLevel.CAN_MANAGE
            )

    # Set permissions on Experiments if necessary
    experiment_ids = _get_experiment_ids_from_trace_artifacts(model_name)
    if permission_level == PermissionLevel.NO_PERMISSIONS:
        _clear_permissions_for_user_experiments(experiment_ids, users)
    elif permission_level == PermissionLevel.CAN_VIEW:
        # If the user previously had any permissions on the experiment delete them
        _clear_permissions_for_user_experiments(experiment_ids, users)
    elif permission_level == PermissionLevel.CAN_QUERY:
        # If the user previously had any permissions on the experiment delete them
        _clear_permissions_for_user_experiments(experiment_ids, users)
    elif permission_level == PermissionLevel.CAN_REVIEW:
        _update_permissions_on_experiment(
            experiment_ids, users, WorkspaceObjectPermissionLevel.CAN_READ
        )
    elif permission_level == PermissionLevel.CAN_MANAGE:
        # If the user previously had any permissions on the experiment delete them
        _update_permissions_on_experiment(
            experiment_ids, users, WorkspaceObjectPermissionLevel.CAN_READ
        )
