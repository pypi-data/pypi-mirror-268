"""Methods and classes for working with configuration files."""

import abc
import dataclasses
from typing import List, Optional

from databricks.rag import constants, entities, environments


_MODEL_JUDGED_ASSESSMENT_NAMES = {
    constants.FAITHFULNESS_METRIC_NAME,
    constants.RELEVANCE_METRIC_NAME,
    constants.ANSWER_CORRECTNESS_METRIC_NAME,
}


@dataclasses.dataclass
class MetricArgs:
    """Metric args"""

    model: Optional[str] = None


@dataclasses.dataclass
class MetricConfig:
    """Metric config"""

    metric_name: str
    metric_args: MetricArgs


class ExtendedConfig(abc.ABC):
    """Interface for extended config for the user input and options in current environment"""

    @property
    @abc.abstractmethod
    def input_config(self) -> entities.Config:
        pass

    @property
    @abc.abstractmethod
    def deployed_environment_info(self) -> Optional[environments.EnvironmentInfo]:
        pass

    @property
    @abc.abstractmethod
    def metric_confs(self) -> List[MetricConfig]:
        pass


class DefaultExtendedConfig(ExtendedConfig):
    """Default implementation of ExtendedConfig"""

    def __init__(
        self, root_path: str, config_path: str, env_name: Optional[str] = None
    ):
        """Initializes an ExtendedConfig.

        Args:
            root_path: The root path where configs are stored
            config_path: The path to the config file relative to the root_path
            env_name: The name of the environment to use
        """
        self._input_config = entities.Config.from_file(f"{root_path}/{config_path}")
        if env_name is None:
            self._deployed_environment_info = None
        else:
            self._deployed_environment_info = environments.get_environment_info(
                self._input_config.global_config.mlflow_experiment_name,
                env_name,
            )

        # Convert the input metric confs (which only contains the judge and metric names)
        # to a list of full metric configuration templates that can be instantiated by the eval notebooks.
        # Note that this will be all shared metric confs; however, the offline eval notebook will need to
        # build additional metric confs for offline-specific assessments like retrieval precision_at_k.
        self._metric_confs = []
        for judge_conf in self._input_config.evaluation.assessment_judges:
            endpoint_name = judge_conf.endpoint_name
            self._metric_confs = [
                MetricConfig(
                    metric_name=assessment_name,
                    # TODO (vperiyasamy): Add examples to the metric args when we support it
                    metric_args=MetricArgs(
                        **(
                            # We only want to pass the model arg for model-judged assessments.
                            dict(model=f"endpoints:/{endpoint_name}")
                            if assessment_name in _MODEL_JUDGED_ASSESSMENT_NAMES
                            else {}
                        )
                    ),
                )
                for assessment_name in judge_conf.assessments
            ]

    @property
    def input_config(self) -> entities.Config:
        return self._input_config

    @property
    def deployed_environment_info(self) -> Optional[environments.EnvironmentInfo]:
        return self._deployed_environment_info

    @property
    def metric_confs(self) -> List[MetricConfig]:
        return self._metric_confs


class MockExtendedConfig(ExtendedConfig):
    """Mock implementation of ExtendedConfig suitable for tests"""

    def __init__(
        self,
        input_config: entities.Config,
        metric_confs: List[MetricConfig],
        deployed_environment_info: Optional[environments.EnvironmentInfo] = None,
    ):
        self._input_config = input_config
        self._deployed_environment_info = deployed_environment_info
        self._metric_confs = metric_confs

    @property
    def input_config(self) -> entities.Config:
        return self._input_config

    @property
    def deployed_environment_info(self) -> Optional[environments.EnvironmentInfo]:
        return self._deployed_environment_info

    @property
    def metric_confs(self) -> List[MetricConfig]:
        return self._metric_confs
