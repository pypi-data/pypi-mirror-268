# IMPORTANT NOTE: Please don't add any other dependencies to this file other than MLflow.
import mlflow
from mlflow.pyfunc import PythonModel
from mlflow.pyfunc import log_model
from mlflow.models.signature import ModelSignature
from mlflow.types import DataType, Schema, ColSpec

_FEEDBACK_MODEL_NAME = "feedback"


class DummyFeedbackModel(PythonModel):
    def predict(self, model_input):
        return {"result": "ok"}


def _load_pyfunc(model_path):
    return DummyFeedbackModel()


def log_feedback_model(feedback_uc_model_name):
    input_schema = Schema(
        [
            ColSpec(DataType.string, "request_id"),
            ColSpec(DataType.string, "source"),
            ColSpec(DataType.string, "text_assessments"),
            ColSpec(DataType.string, "retrieval_assessments"),
        ]
    )
    output_schema = Schema([ColSpec(DataType.string, "result")])
    input_signature = ModelSignature(inputs=input_schema, outputs=output_schema)

    with mlflow.start_run(run_name="feedback-model"):
        return log_model(
            artifact_path=_FEEDBACK_MODEL_NAME,
            signature=input_signature,
            loader_module="feedback",
            pip_requirements=[
                f"mlflow=={mlflow.__version__}",
            ],
            registered_model_name=feedback_uc_model_name,
            code_path=[__file__],
        )
