import dataclasses
from typing import Optional, Mapping

import copy
import mlflow
import json

from databricks.rag import entities
from databricks.rag.constants import (
    MLFLOW_RAG_APP_TAG,
    MLFLOW_RAG_APP_GLOBAL_CONFIG_TAG,
    EnvironmentName,
)


@dataclasses.dataclass
class EnvironmentInfo:
    """
    Info for a deployed environment
    """

    endpoint_name: str
    request_log_table: str
    assessment_log_table: str
    model_name: str
    workspace_folder: str
    secret_scope: str
    secret_key: str
    security_scope: Optional[str] = (
        None  # Deprecated, please use the new secret_scope instead
    )
    security_key: Optional[str] = (
        None  # Deprecated, please use the new secret_scope instead
    )
    cluster_id: Optional[str] = None
    owner: Optional[str] = None


def _create_info(
    config: entities.Config, environment: str, owner: Optional[str] = None
) -> EnvironmentInfo:
    """
    Get the config for a given environment
    :param config: The parsed configuration used to create environment.
    :param environment: environment string.

    :return: The config that contains the global_config and the environment specific config.
    """
    global_config = config.global_config
    all_environments_config = config.environment_config
    catalog_name = global_config.uc_assets_location.catalog
    schema_name = global_config.uc_assets_location.schema
    app_name = global_config.name

    derived_config = {
        "endpoint_name": f"rag_studio_{app_name}_{environment}",
        "request_log_table": f"{catalog_name}.{schema_name}.rag_studio_{app_name}_{environment}_request_log",
        "assessment_log_table": f"{catalog_name}.{schema_name}.rag_studio_{app_name}_{environment}_assessment_log",
        "model_name": get_model_name(config),
    }
    if environment in [EnvironmentName.END_USERS, EnvironmentName.REVIEWERS]:
        environment_config = getattr(all_environments_config, environment)
    else:
        environment_config = next(
            (
                dev_config
                for dev_config in all_environments_config.development
                if dev_config.name == environment
            ),
            None,
        )

    if environment_config is None:
        raise ValueError(f"Environment {environment} not found in config {config}")

    return EnvironmentInfo(
        **derived_config,
        workspace_folder=environment_config.workspace_folder,
        security_key=(
            environment_config.security_key
            if hasattr(environment_config, "security_key")
            else None
        ),
        security_scope=(
            environment_config.security_scope
            if hasattr(environment_config, "security_scope")
            else None
        ),
        secret_key=environment_config.secret_key,
        secret_scope=environment_config.secret_scope,
        cluster_id=(
            environment_config.cluster_id
            if hasattr(environment_config, "cluster_id")
            else None
        ),
        owner=owner,
    )


def create_environment(
    config: entities.Config, env_name: str, owner: Optional[str] = None
) -> None:
    """
    Create an environment based on the config file in a given experiment

    :param config: The parsed configuration used to create environment.
    :param env_name: environment string.
    """
    # Parse the config file
    environment_info = _create_info(config, env_name, owner)
    global_config = config.global_config
    experiment_name = global_config.mlflow_experiment_name
    experiment = mlflow.get_experiment_by_name(experiment_name)
    env_tag = f"{MLFLOW_RAG_APP_TAG}_{env_name}"

    if experiment:
        mlflow.set_experiment(experiment_name)
        if env_tag in experiment.tags:
            # If this is a production environment and it already exists then exit -- nothing to do here.
            if env_name in [EnvironmentName.END_USERS, EnvironmentName.REVIEWERS]:
                return

            if owner is None:
                raise ValueError(
                    f"Environment {env_name} should have the owner field passed in"
                )
            existing_info = get_environment_info(experiment_name, env_name)

            if existing_info.owner != owner:
                raise ValueError(
                    f"Environment {env_name} already exists in experiment {experiment_name} under owner {existing_info.owner}"
                )
            # Do a no-op if the environment already exists for an owner
        else:
            mlflow.set_experiment_tags(
                {env_tag: json.dumps(dataclasses.asdict(environment_info))}
            )
    else:
        mlflow.create_experiment(
            experiment_name,
            tags={
                env_tag: json.dumps(dataclasses.asdict(environment_info)),
                MLFLOW_RAG_APP_GLOBAL_CONFIG_TAG: json.dumps(
                    dataclasses.asdict(global_config)
                ),
            },
        )
        mlflow.set_experiment(experiment_name)


def _resolve_secret_scope_key(
    environment_config: Mapping[str, str]
) -> Mapping[str, str]:
    # Check if either 'secret_key' or 'security_key' exists in environment_config
    secret_key = environment_config.get(
        "secret_key",
        environment_config.get("security_key", None),
    )

    # Check if either 'secret_scope' or 'security_scope' exists in environment_config
    secret_scope = environment_config.get(
        "secret_scope",
        environment_config.get("security_scope", None),
    )

    return {
        "secret_scope": secret_scope,
        "secret_key": secret_key,
    }


def get_environment_info(experiment_name: str, environment: str) -> EnvironmentInfo:
    """
    Retrieve config for a specific environment from the experiment.
    :param experiment_name: The name of the experiment.
    :param environment: environment string.

    :return: Environment specific config.
    """
    experiment = mlflow.get_experiment_by_name(experiment_name)

    if not experiment:
        raise ValueError(
            f"Experiment {experiment_name} does not exist, please setup the experiment first."
        )

    env_tag = f"{MLFLOW_RAG_APP_TAG}_{environment}"
    if env_tag not in experiment.tags:
        raise ValueError(
            f"Environment {environment} does not exist in experiment {experiment_name}"
        )

    environment_config = copy.deepcopy(json.loads(experiment.tags[env_tag]))
    environment_config.update(**_resolve_secret_scope_key(environment_config))

    return EnvironmentInfo(**environment_config)


def get_model_name(config: entities.Config):
    """
    Returns the model name for the given config
    :param config: The parsed configuration used to fetch the model name from.
    """
    global_config = config.global_config
    catalog_name = global_config.uc_assets_location.catalog
    schema_name = global_config.uc_assets_location.schema
    app_name = global_config.name

    return f"{catalog_name}.{schema_name}.rag_studio_{app_name}"
