import datetime
import json
import pytest
from unittest import mock

from pyspark.sql import Row, functions as F, types as T

from databricks.rag.evaluation.offline import (
    add_labels_to_eval_dataset,
    generate_offline_predictions,
)
from databricks.rag.unpacking.schemas import (
    CHOICES_SCHEMA,
    EVAL_DATASET_INPUT_SCHEMA,
    EVAL_DATASET_OUTPUT_SCHEMA,
)
from tests.unpacking.eval_test_utils import schemas_equal


@pytest.fixture
def model_name():
    return "test_model"


@pytest.fixture
def model_version():
    return "1"


@pytest.fixture
def unlabeled_eval_dataset(spark):
    # return a spark dataframe with unlabeled eval data
    # this dataframe should contain 1 column called "request"
    # the "request" column should contain a struct with a field "messages" which is a MESSAGE_SCHEMA
    unlabeled_eval_dataset = spark.createDataFrame(
        [
            {
                "request": {
                    "messages": [
                        {
                            "role": "user",
                            "content": "What did the president say about the economy?",
                        }
                    ]
                }
            },
            {
                "request": {
                    "messages": [
                        {"role": "system", "content": "Respond in one sentence."},
                        {
                            "role": "user",
                            "content": "What is the capital of France?",
                        },
                    ]
                }
            },
        ],
        schema=EVAL_DATASET_INPUT_SCHEMA,
    )
    return unlabeled_eval_dataset


@pytest.fixture()
def labeled_eval_dataset(spark):
    labeled_eval_dataset = spark.createDataFrame(
        [
            {
                "request": {
                    "messages": [
                        {
                            "role": "user",
                            "content": "What did the president say about the economy?",
                        }
                    ]
                },
                "ground_truth": {
                    "text_output": {
                        "content": "The president said the following about the economy"
                    },
                    "retrieval_output": {
                        "chunks": [
                            {
                                "doc_uri": "state_of_the_union.txt",
                                "content": "foobar",
                            }
                        ]
                    },
                },
            },
            {
                "request": {
                    "messages": [
                        {
                            "role": "system",
                            "content": "Respond in one sentence.",
                        },
                        {
                            "role": "user",
                            "content": "What is the capital of France?",
                        },
                    ]
                },
                "ground_truth": {
                    "text_output": {"content": "The capital of France is Paris"},
                    "retrieval_output": {
                        "chunks": [
                            {
                                "doc_uri": "state_of_the_union.txt",
                                "content": "FooBar1",
                            },
                            {
                                "doc_uri": "state_of_the_union.txt",
                                "content": "FooBar2",
                            },
                        ]
                    },
                },
            },
        ],
        schema=EVAL_DATASET_INPUT_SCHEMA,
    )
    return labeled_eval_dataset


dummy_response = {"choices": [{"message": {"content": "My Dummy Response"}}]}
dummy_traces = json.dumps(
    {
        "steps": [
            {
                "name": "Retriever",
                "type": "RETRIEVAL",
                "start_timestamp": "2024-01-11T19:55:57.586159",
                "end_timestamp": "2024-01-11T19:55:58.372986",
                "retrieval": {
                    "query_text": "What did the president say about the economy?",
                    "chunks": [
                        {
                            "chunk_id": "a0251297-78e4-407c-aeb4-7bb6410ccc2d",
                            "doc_uri": "state_of_the_union.txt",
                            "content": "FooBar1",
                        },
                        {
                            "chunk_id": "21a53baa-65b0-450d-8d38-6314eb8a2383",
                            "doc_uri": "state_of_the_union.txt",
                            "content": "FooBar2",
                        },
                        {
                            "chunk_id": "5879676d-0eb3-48ae-aa30-5aeede714e36",
                            "doc_uri": "state_of_the_union.txt",
                            "content": "FooBar3",
                        },
                        {
                            "chunk_id": "a0c3cad6-0f34-4826-9a1b-a9d940fef876",
                            "doc_uri": "state_of_the_union.txt",
                            "content": "FooBar4",
                        },
                    ],
                },
                "text_generation": None,
                "error": None,
                "step_id": "24b94276-0cf5-41f3-bacc-7aece56fbb2e",
            },
            {
                "name": "LLM",
                "type": "LLM_GENERATION",
                "start_timestamp": "2024-01-11T19:55:58.374143",
                "end_timestamp": "2024-01-11T19:56:07.463793",
                "retrieval": None,
                "text_generation": {
                    "prompt": "Human: ",
                    "generated_text": "FooBaz",
                },
                "error": None,
                "step_id": "85ad2ea6-dbe8-4d14-8fc8-09dcc90aad60",
            },
        ],
        "start_timestamp": "2024-01-11T19:55:57.586159",
        "end_timestamp": "2024-01-11T19:56:07.463793",
        "is_truncated": False,
    }
)


def _overwrite_nullability_for_testing(schema):
    schema["output"].dataType["choices"].dataType = CHOICES_SCHEMA
    schema["trace"].dataType["app_version_id"].nullable = True
    schema["trace"].nullable = True
    return schema


def test_generate_offline_predictions_unlabeled(
    unlabeled_eval_dataset, model_name, model_version
):
    # mock the call to rag.invoke
    with mock.patch(
        "databricks.rag.evaluation.offline._invoke_with_chain",
        return_value=(dummy_response, dummy_traces),
    ):
        offline_predictions = generate_offline_predictions(
            unlabeled_eval_dataset, "test_chain", model_name, model_version
        )
        schema = offline_predictions.schema
        schema = _overwrite_nullability_for_testing(schema)

        assert schema == EVAL_DATASET_OUTPUT_SCHEMA
        assert offline_predictions.count() == 2

        offline_predictions_values = offline_predictions.collect()[0].asDict()
        assert offline_predictions_values["request"]["messages"] == [
            Row(role="user", content="What did the president say about the economy?")
        ]
        assert (
            offline_predictions_values["trace"].asDict()["app_version_id"]
            == "models:/test_model/1"
        )
        assert offline_predictions_values["trace"].asDict()["steps"] == [
            Row(
                step_id="24b94276-0cf5-41f3-bacc-7aece56fbb2e",
                name="Retriever",
                type="RETRIEVAL",
                start_timestamp=datetime.datetime(2024, 1, 11, 19, 55, 57, 586159),
                end_timestamp=datetime.datetime(2024, 1, 11, 19, 55, 58, 372986),
                retrieval=Row(
                    query_text="What did the president say about the economy?",
                    chunks=[
                        Row(
                            chunk_id="a0251297-78e4-407c-aeb4-7bb6410ccc2d",
                            doc_uri="state_of_the_union.txt",
                            content="FooBar1",
                        ),
                        Row(
                            chunk_id="21a53baa-65b0-450d-8d38-6314eb8a2383",
                            doc_uri="state_of_the_union.txt",
                            content="FooBar2",
                        ),
                        Row(
                            chunk_id="5879676d-0eb3-48ae-aa30-5aeede714e36",
                            doc_uri="state_of_the_union.txt",
                            content="FooBar3",
                        ),
                        Row(
                            chunk_id="a0c3cad6-0f34-4826-9a1b-a9d940fef876",
                            doc_uri="state_of_the_union.txt",
                            content="FooBar4",
                        ),
                    ],
                ),
                text_generation=None,
            ),
            Row(
                step_id="85ad2ea6-dbe8-4d14-8fc8-09dcc90aad60",
                name="LLM",
                type="LLM_GENERATION",
                start_timestamp=datetime.datetime(2024, 1, 11, 19, 55, 58, 374143),
                end_timestamp=datetime.datetime(2024, 1, 11, 19, 56, 7, 463793),
                retrieval=None,
                text_generation=Row(prompt="Human: ", generated_text="FooBaz"),
            ),
        ]
        assert offline_predictions_values["output"] == Row(
            choices=[Row(message=Row(role="assistant", content="My Dummy Response"))]
        )
        assert offline_predictions_values["ground_truth"] is None


def test_generate_offline_predictions_labeled(
    labeled_eval_dataset, model_name, model_version
):
    # mock the call to rag.invoke
    with mock.patch(
        "databricks.rag.evaluation.offline._invoke_with_chain",
        return_value=(dummy_response, dummy_traces),
    ):
        offline_predictions = generate_offline_predictions(
            labeled_eval_dataset, "test_chain", model_name, model_version
        )
        schema = offline_predictions.schema
        schema = _overwrite_nullability_for_testing(schema)

        assert schema == EVAL_DATASET_OUTPUT_SCHEMA
        assert offline_predictions.count() == 2

        offline_predictions_values = offline_predictions.collect()[0].asDict()
        assert offline_predictions_values["request"]["messages"] == [
            Row(role="user", content="What did the president say about the economy?")
        ]
        assert (
            offline_predictions_values["trace"].asDict()["app_version_id"]
            == "models:/test_model/1"
        )
        assert offline_predictions_values["trace"].asDict()["steps"] == [
            Row(
                step_id="24b94276-0cf5-41f3-bacc-7aece56fbb2e",
                name="Retriever",
                type="RETRIEVAL",
                start_timestamp=datetime.datetime(2024, 1, 11, 19, 55, 57, 586159),
                end_timestamp=datetime.datetime(2024, 1, 11, 19, 55, 58, 372986),
                retrieval=Row(
                    query_text="What did the president say about the economy?",
                    chunks=[
                        Row(
                            chunk_id="a0251297-78e4-407c-aeb4-7bb6410ccc2d",
                            doc_uri="state_of_the_union.txt",
                            content="FooBar1",
                        ),
                        Row(
                            chunk_id="21a53baa-65b0-450d-8d38-6314eb8a2383",
                            doc_uri="state_of_the_union.txt",
                            content="FooBar2",
                        ),
                        Row(
                            chunk_id="5879676d-0eb3-48ae-aa30-5aeede714e36",
                            doc_uri="state_of_the_union.txt",
                            content="FooBar3",
                        ),
                        Row(
                            chunk_id="a0c3cad6-0f34-4826-9a1b-a9d940fef876",
                            doc_uri="state_of_the_union.txt",
                            content="FooBar4",
                        ),
                    ],
                ),
                text_generation=None,
            ),
            Row(
                step_id="85ad2ea6-dbe8-4d14-8fc8-09dcc90aad60",
                name="LLM",
                type="LLM_GENERATION",
                start_timestamp=datetime.datetime(2024, 1, 11, 19, 55, 58, 374143),
                end_timestamp=datetime.datetime(2024, 1, 11, 19, 56, 7, 463793),
                retrieval=None,
                text_generation=Row(prompt="Human: ", generated_text="FooBaz"),
            ),
        ]
        assert offline_predictions_values["output"] == Row(
            choices=[Row(message=Row(role="assistant", content="My Dummy Response"))]
        )
        assert offline_predictions_values["ground_truth"] == Row(
            text_output=Row(
                content="The president said the following about the economy"
            ),
            retrieval_output=Row(
                name=None,
                chunks=[
                    Row(
                        chunk_id=None,
                        doc_uri="state_of_the_union.txt",
                        content="foobar",
                    )
                ],
            ),
        )


@pytest.fixture()
def setup_unlabeled_eval_table(spark):
    unlabeled_eval_table = [
        {
            "request": {
                "request_id": "12345",
                "messages": [{"role": "user", "content": "What is databricks?"}],
            }
        },
    ]
    unlabeled_eval_df = spark.createDataFrame(
        unlabeled_eval_table, EVAL_DATASET_INPUT_SCHEMA
    )
    unlabeled_eval_df.write.mode("overwrite").format("delta").saveAsTable("eval_table")


@pytest.mark.parametrize(
    "data, expected_doc_count",
    [
        # Test case 1: Two document IDs
        (
            {
                "id": "12345",
                "answer": "Databricks is amazing!",
                "doc_ids": "foo.txt, bar.txt",
            },
            2,
        ),
        # Test case 2: One document ID
        (
            {
                "id": "12345",
                "answer": "Spark is fast!",
                "doc_ids": "baz.txt",
            },
            1,
        ),
        # Test case 3: No document IDs
        (
            {
                "id": "12345",
                "answer": "Python is versatile!",
                "doc_ids": "",
            },
            0,
        ),
    ],
)
def test_add_labels_to_eval_dataset_properly_formed(
    spark, data, expected_doc_count, setup_unlabeled_eval_table
):
    """
    Test the the function can create a ground truth column in the eval table with various number of document IDs
    """
    flat_table_df = spark.createDataFrame(
        [data],
        schema=T.StructType(
            [
                T.StructField("id", T.StringType(), True),
                T.StructField("answer", T.StringType(), True),
                T.StructField("doc_ids", T.StringType(), True),
            ]
        ),
    )
    add_labels_to_eval_dataset(flat_table_df, "eval_table")

    # read the eval table
    eval_dataset_df = spark.read.format("delta").table("eval_table")

    # Check the total number of rows
    assert eval_dataset_df.count() == 1

    # Check the ground truth column
    assert (
        eval_dataset_df.collect()[0]["ground_truth"]["text_output"]["content"]
        == data["answer"]
    )

    # Check the number of document IDs and their content
    chunks = eval_dataset_df.select(
        F.explode("ground_truth.retrieval_output.chunks").alias("chunk")
    ).collect()
    assert len(chunks) == expected_doc_count
    for chunk in chunks:
        assert chunk["chunk"]["doc_uri"] in data["doc_ids"].split(",")

    # Check if the schema matches the expected schema
    assert schemas_equal(eval_dataset_df.schema, EVAL_DATASET_INPUT_SCHEMA)


@pytest.mark.parametrize(
    "data, missing_col",
    [
        # Test case 1: Missing "id"
        (
            {
                "answer": "Databricks is amazing!",
                "doc_ids": "foo.txt, bar.txt",
            },
            "id",
        ),
        # Test case 2: Missing "answer"
        (
            {
                "id": "12345",
                "doc_ids": "baz.txt",
            },
            "answer",
        ),
        # Test case 3: Missing "doc_ids"
        (
            {
                "id": "12345",
                "answer": "Python is versatile!",
            },
            "doc_ids",
        ),
    ],
)
def test_add_labels_to_eval_dataset_missing_columns(
    spark, data, missing_col, setup_unlabeled_eval_table
):
    """
    Test that the function will throw if the input table is missing any of the required columns
    """
    flat_table_df = spark.createDataFrame([data])
    with pytest.raises(ValueError, match=f"Column {missing_col} is required"):
        add_labels_to_eval_dataset(flat_table_df, "eval_table")


@pytest.fixture()
def setup_partially_labeled_eval_table(spark):
    partially_labeled_eval_table = [
        {
            "request": {
                "request_id": "12345",
                "messages": [{"role": "user", "content": "What is databricks?"}],
            },
            "ground_truth": {
                "text_output": {"content": "Databricks is amazing!"},
                "retrieval_output": {
                    "chunks": [
                        {
                            "doc_uri": "foo.txt",
                        }
                    ],
                },
            },
        },
        {
            "request": {
                "request_id": "12346",
                "messages": [{"role": "user", "content": "What is databricks?"}],
            },
        },
        {
            "request": {
                "request_id": "12347",
                "messages": [
                    {"role": "user", "content": "What is Databricks' mission?"}
                ],
            },
        },
        {
            "request": {
                "request_id": "12348",
                "messages": [
                    {"role": "user", "content": "Where are Databricks' founders from?"}
                ],
            },
            "ground_truth": {
                "text_output": {"content": "UC Berkeley"},
                "retrieval_output": {
                    "chunks": [
                        {
                            "doc_uri": "foo.txt",
                        }
                    ],
                },
            },
        },
    ]
    partially_labeled_eval_df = spark.createDataFrame(
        partially_labeled_eval_table, EVAL_DATASET_INPUT_SCHEMA
    )
    partially_labeled_eval_df.write.mode("overwrite").format("delta").saveAsTable(
        "eval_table"
    )


def test_add_labels_to_eval_dataset_partially_filled(
    spark, setup_partially_labeled_eval_table
):
    """
    Test that the function will add the labeled ground truth to the eval table if it does not exist,
    update the existing ground truth if it exists, and leave the rows not in the flat table unaffected
    """
    flat_table = spark.createDataFrame(
        [
            # Overwrite the ground truth for request_id 12345
            {
                "id": "12345",
                "answer": "Databricks is super amazing!",
                "doc_ids": "foo.txt",
            },
            # Add the ground truth for request_id 12346
            {
                "id": "12346",
                "answer": "Databricks is the data and ai company!",
                "doc_ids": "bar.txt",
            },
        ],
        schema=T.StructType(
            [
                T.StructField("id", T.StringType(), True),
                T.StructField("answer", T.StringType(), True),
                T.StructField("doc_ids", T.StringType(), True),
            ]
        ),
    )
    add_labels_to_eval_dataset(flat_table, "eval_table")

    # read the eval table and order by request_id for test
    eval_dataset_df = (
        spark.read.format("delta").table("eval_table").orderBy("request.request_id")
    )

    # Check the total number of rows
    # TODO (prithvi): update this to not depend on order
    assert eval_dataset_df.count() == 4

    eval_dataset_0 = eval_dataset_df.collect()[0].asDict()
    eval_dataset_1 = eval_dataset_df.collect()[1].asDict()
    eval_dataset_2 = eval_dataset_df.collect()[2].asDict()
    eval_dataset_3 = eval_dataset_df.collect()[3].asDict()

    assert (
        eval_dataset_0["ground_truth"]["text_output"]["content"]
        == "Databricks is super amazing!"
    )
    assert (
        eval_dataset_0["ground_truth"]["retrieval_output"]["chunks"][0]["doc_uri"]
        == "foo.txt"
    )

    assert (
        eval_dataset_1["ground_truth"]["text_output"]["content"]
        == "Databricks is the data and ai company!"
    )
    assert (
        eval_dataset_1["ground_truth"]["retrieval_output"]["chunks"][0]["doc_uri"]
        == "bar.txt"
    )

    assert eval_dataset_2["ground_truth"] is None

    assert eval_dataset_3["ground_truth"]["text_output"]["content"] == "UC Berkeley"

    assert (
        eval_dataset_3["ground_truth"]["retrieval_output"]["chunks"][0]["doc_uri"]
        == "foo.txt"
    )
