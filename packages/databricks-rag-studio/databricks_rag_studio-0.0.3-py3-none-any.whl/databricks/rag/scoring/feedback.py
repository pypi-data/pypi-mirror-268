import mlflow.pyfunc

from mlflow.models.signature import ModelSignature
from mlflow.types import DataType, Schema, ColSpec
from typing import Optional

from mlflow.utils.annotations import deprecated

from databricks.rag import configs
from databricks.rag.entities import UnityCatalogModel
from databricks.rag.utils import mlflow as mlflow_utils


class FeedbackModel:
    """
    Feedback model class that creates a feedback model and logs it to MLflow

    :param extended_config: config mapping from the dab config file
    """

    _FEEDBACK_MODEL_NAME = "feedback"

    def __init__(
        self,
        extended_config: configs.ExtendedConfig,
        feedback_model: Optional[mlflow.pyfunc.PythonModel] = None,
    ):
        input_config = extended_config.input_config
        global_config = input_config.global_config
        experiment_name = global_config.mlflow_experiment_name
        self.catalog_name = global_config.uc_assets_location.catalog
        self.schema_name = global_config.uc_assets_location.schema

        if feedback_model is None:
            model = PyfuncFeedbackModel()
            pip_requirements = [
                "mlflow>=2.10.0",
                "https://ml-team-public-read.s3.us-west-2.amazonaws.com/wheels/rag-studio/ed24b030-3c87-40b1-b04c-bb1977254aa3/databricks_rag-0.0.0a1-py3-none-any.whl",
            ]
        else:
            model = feedback_model
            pip_requirements = [
                "mlflow>=2.10.0",
            ]

        feedback_model_version = mlflow_utils.get_latest_model_version(
            self.uc_model.full_name(
                use_backtick_delimiters=False
            )  # mlflow handles the escaping
        )
        if feedback_model_version > 0:
            print("Feedback model already exists, nothing created")
            return

        # Define the input and output protobuf messages for the signature
        input_schema = Schema(
            [
                ColSpec(DataType.string, "request_id"),
                ColSpec(DataType.string, "source"),
                ColSpec(DataType.string, "text_assessments"),
                ColSpec(DataType.string, "retrieval_assessments"),
            ]
        )
        output_schema = Schema([ColSpec(DataType.string, "result")])

        # Create a ModelSignature
        input_signature = ModelSignature(inputs=input_schema, outputs=output_schema)

        mlflow.set_experiment(experiment_name)
        mlflow.set_registry_uri("databricks-uc")

        with mlflow.start_run(run_name="feedback-model"):
            # Log the model with the specified signature
            mlflow.pyfunc.log_model(
                artifact_path=self._FEEDBACK_MODEL_NAME,
                python_model=model,
                signature=input_signature,
                pip_requirements=pip_requirements,
                registered_model_name=self.uc_model.full_name(
                    use_backtick_delimiters=False  # mlflow handles the escaping
                ),
            )

    @property
    @deprecated("Use `uc_model` instead")
    def name(self) -> str:
        """Get the non-delimited full name of the feedback model in UC."""
        return self.uc_model.full_name(use_backtick_delimiters=False)

    @property
    def uc_model(self) -> UnityCatalogModel:
        """Get the Unity Catalog model entity of the feedback model."""
        return UnityCatalogModel(
            catalog_name=self.catalog_name,
            schema_name=self.schema_name,
            model_name=self._FEEDBACK_MODEL_NAME,
        )


class PyfuncFeedbackModel(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input) -> dict:
        return {"result": "ok"}
