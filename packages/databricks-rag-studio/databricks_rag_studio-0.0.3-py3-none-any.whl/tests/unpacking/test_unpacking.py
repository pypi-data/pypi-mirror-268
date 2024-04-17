import datetime
import pandas as pd
import pytest
from pyspark.sql import types as T

from databricks.rag.unpacking import unpack_and_split_payloads
from databricks.rag.unpacking.schemas import (
    ASSESSMENT_LOG_SCHEMA,
    REQUEST_LOG_SCHEMA,
    REQUEST_LOG_V2_SCHEMA,
)

from .eval_test_utils import schemas_equal

_INFERENCE_TABLE_PAYLOD_SCHEMA = T.StructType(
    [
        T.StructField("client_request_id", T.StringType()),
        T.StructField("databricks_request_id", T.StringType()),
        T.StructField("date", T.DateType()),
        T.StructField("timestamp_ms", T.LongType()),
        T.StructField("status_code", T.StringType()),
        T.StructField("execution_time_ms", T.LongType()),
        T.StructField("request", T.StringType()),
        T.StructField("response", T.StringType()),
        T.StructField("sampling_fraction", T.DoubleType()),
        T.StructField("request_metadata", T.StringType()),
    ]
)


@pytest.fixture()
def sample_requests():
    return [
        # A RAG request
        """
            {
              "messages": [
                {
                  "role": "user",
                  "content": "Is mlflow good?"
                }
              ],
              "databricks_options": {
                "return_trace": true,
                "conversation_id": "123456"
              }
            }
            """,
        # A text assessment request
        """
            {
              "dataframe_records": [
                {
                  "request_id": "24680",
                  "source" : {
                    "type": "end_user",
                    "id" : "alkis"
                  },
                  "text_assessments": [{
                    "step_id": "0123",
                    "ratings": {
                      "harmful": {
                        "value": true,
                        "rationale": "too mean"
                      }
                    },
                    "suggested_output": "We have 2 months of vacation",
                    "free_text_comment": "I really didn't like the answer because..."
                  }]
                }
              ]
            }
            """,
        # A retrieval assessment request with multiple assessments
        """
            {
              "dataframe_records": [
                {
                  "request_id": "35209",
                  "source" : {
                    "type": "expert",
                    "id" : "ali-ghodsi"
                  },
                  "retrieval_assessments": [
                    {
                      "step_id": "0123",
                      "position": 0,
                      "ratings": {
                        "relevant": {
                          "value": false,
                          "rationale": "too long"
                        }
                      },
                      "free_text_comment": "I'm leaving a comment!"
                    },
                    {
                      "step_id": "0123",
                      "position": 1,
                      "ratings": {
                        "relevant": {
                          "value": true,
                          "rationale": "spot on"
                        }
                      }
                    }
                  ]
                }
              ]
            }
            """,
        # An erroneous request that will be filtered out
        "blah",
        # An assessment request with both text and retrieval assessments
        """
            {
              "dataframe_records": [
                {
                  "request_id": "729962",
                  "source" : {
                    "type": "expert",
                    "id" : "corey_zumar",
                    "tags": {}
                  },
                  "text_assessments": [{
                    "step_id": "012233",
                    "ratings": {
                      "faithfulness": {
                        "value": false,
                        "rationale": "unfaithful"
                      }
                    }
                  }],
                  "retrieval_assessments": [
                    {
                      "step_id": "0123",
                      "position": 0,
                      "ratings": {
                        "relevant": {
                          "value": false,
                          "rationale": "too long"
                        }
                      },
                      "free_text_comment": "I'm leaving a comment!"
                    },
                    {
                      "step_id": "0123",
                      "position": 1,
                      "ratings": {
                        "faithful": {
                          "value": true,
                          "rationale": "spot on"
                        }
                      }
                    }
                  ]
                }
              ]
            }
            """,
    ]


@pytest.fixture()
def sample_rag_response():
    return """
            {
              "object": "chat.completion",
              "created": 1705451212,
              "choices": [
                {
                  "index": 0,
                  "message": {"role": "assistant", "content": "MLflow is amazing!"}
                }
              ],
              "id": "12345",
              "databricks_output" : {
                "trace": {
                  "app_version_id": "avi123",
                  "start_timestamp": "2024-01-03T19:51:10.686454",
                  "end_timestamp": "2024-01-03T19:51:24.932795",
                  "is_truncated": false,
                  "steps": [
                      {
                        "step_id": "29470854",
                        "name": "Retriever",
                        "type": "RETRIEVAL",
                        "retrieval": {
                          "query_text": "What did the president say about the economy?",
                          "chunks": [
                            {
                              "chunk_id": "a0251297-78e4-407c-aeb4-7bb6410ccc2d",
                              "content": "Vice President Harris and I ran for office with a new vision for America.",
                              "doc_uri": null
                            },
                            {
                              "chunk_id": "21a53baa-65b0-450d-8d38-6314eb8a2383",
                              "content": "And so many families are living paycheck to paycheck, struggling to keep up...",
                              "doc_uri": null
                            }
                          ]
                        },
                        "start_timestamp": "2024-01-03T19:51:10.686454",
                        "end_timestamp": "2024-01-03T19:51:11.290311"
                      },
                      {
                        "step_id": "00928383",
                        "name": "LLM",
                        "type": "LLM_GENERATION",
                        "text_generation": {
                          "prompt": "Human",
                          "generated_text": "The president"
                        },
                        "start_timestamp": "2024-01-03T19:51:11.292079",
                        "end_timestamp": "2024-01-03T19:51:24.932795"
                      },
                      {
                        "step_id": "87620983",
                        "name": "LLM",
                        "type": "LLM_GENERATION",
                        "text_generation": {
                          "prompt": "Human",
                          "generated_text": "The president"
                        },
                        "start_timestamp": "2024-01-03T19:51:11.292079",
                        "end_timestamp": "2024-01-03T19:51:24.932795"
                      }
                  ]
                }
              }
            }
            """


def sample_payload_logs(spark, sample_requests, rag_response):
    payload_data = {
        "client_request_id": [None, None, None, None, None],
        "databricks_request_id": ["12345", "67890", "099883", "204838", "709714"],
        "date": [
            datetime.date(2023, 1, 1),
            datetime.date(2023, 1, 2),
            datetime.date(2023, 1, 3),
            datetime.date(2023, 1, 4),
            datetime.date(2023, 1, 5),
        ],
        "timestamp_ms": [
            1609459200000,
            1609459200001,
            1609459200002,
            1609459200003,
            1609459200004,
        ],
        "status_code": ["200", "200", "200", "404", "200"],
        "execution_time_ms": [37, 73, 92, 22, 11],
        "request": sample_requests,
        "response": [
            # A RAG response
            rag_response,
            # A text assessment response
            "",
            # A retrieval assessment response
            "",
            # An erroneous request response
            "",
            # A text and retrieval assessment response
            "",
        ],
        "sampling_fraction": [1.0, 1.0, 1.0, 1.0, 1.0],
        "request_metadata": [None, None, None, None, None],
    }
    return spark.createDataFrame(
        pd.DataFrame(payload_data),
        _INFERENCE_TABLE_PAYLOD_SCHEMA,
    )


# Our unpacking logic uses edge Spark features, namely the ":" query notation for semi-structured data.
@pytest.mark.edge_spark
def test_unpack_and_split_payloads(spark, sample_requests, sample_rag_response):
    payloads = sample_payload_logs(spark, sample_requests, sample_rag_response)
    request_log, assessment_log = unpack_and_split_payloads(payloads)

    # Check that the schema of the resulting DataFrames is correct
    assert schemas_equal(request_log.schema, REQUEST_LOG_SCHEMA)
    assert schemas_equal(assessment_log.schema, ASSESSMENT_LOG_SCHEMA)

    # Check the row counts for the resulting DataFrames
    # We have 5 payloads in the sample data, but 1 is an erroneous request that will be filtered out
    # The request payload results in 1 row
    # The text assessment payload results in 1 row +
    # The retrieval assessment payload results in 2 rows +
    # The combined assessment payload results in 3 more rows (1 text + 2 retrieval)
    expected_request_log_count = 1
    expected_assessment_log_count = 1 + 2 + (1 + 2)
    request_log_count = request_log.count()
    assessment_log_count = assessment_log.count()
    assert (
        request_log_count == expected_request_log_count
    ), f"expected {expected_request_log_count} rows, got {request_log_count}"
    assert (
        assessment_log_count == expected_assessment_log_count
    ), f"expected {expected_assessment_log_count} rows, got {assessment_log_count}"

    # Spot check a few values in the request log
    request_log_values = request_log.collect()[0].asDict()
    assert request_log_values["request"]["last_input"] == "Is mlflow good?"
    assert (
        request_log_values["trace"]["steps"][0]["retrieval"]["chunks"][0]["content"]
        == "Vice President Harris and I ran for office with a new vision for America."
    )
    assert (
        request_log_values["output"]["choices"][0]["message"]["content"]
        == "MLflow is amazing!"
    )

    # Spot check a few values in the assessment log
    assessment_log_values = assessment_log.collect()[0].asDict()
    assert (
        assessment_log_values["text_assessment"]["ratings"]["harmful"]["rationale"]
        == "too mean"
    )
    assert assessment_log_values["retrieval_assessment"] is None


@pytest.fixture()
def sample_rag_response_v2():
    return """
            {
              "object": "chat.completion",
              "created": 1705451212,
              "choices": [
                {
                  "index": 0,
                  "message": {"role": "assistant", "content": "MLflow is amazing!"}
                }
              ],
              "id": "12345",
              "databricks_output" : {
                "trace": {
                  "app_version_id": "avi123",
                  "mlflow.trace_schema.version": 2,
                  "start_timestamp": "2024-01-03T19:51:10.686454",
                  "end_timestamp": "2024-01-03T19:51:24.932795",
                  "is_truncated": false,
                  "spans": [
                    {
                      "name": "RetrievalQA",
                      "context": {"request_id": "", "span_id": "1c04bf28-8c29-42b1-9530-c8836f692806"},
                      "status": {"status_code": "OK", "description": ""},
                      "span_type": "CHAIN",
                      "start_time": "2024-03-21T11:14:00.655056+00:00",
                      "end_time": "2024-03-21T11:14:02.901672+00:00",
                      "parent_span_id": null,
                      "inputs": "{'query': 'What did the president say about Ketanji Brown Jackson'}",
                      "outputs": "{'result': 'Nothing in these pieces of context mentions her.'}",
                      "attributes": "{}",
                      "events": [
                        {"name": "start", "timestamp": "2024-03-21T11:14:00.655056+00:00", "attributes": "{}"},
                        {"name": "end", "timestamp": "2024-03-21T11:14:02.901672+00:00", "attributes": "{}"}
                      ]
                    },
                    {
                      "name": "Retriever",
                      "context": {"request_id": "", "span_id": "be08fa85-ac18-4ce4-b7e7-7bad0ef8b004"},
                      "status": {"status_code": "OK", "description": ""},
                      "span_type": "RETRIEVER",
                      "start_time": "2024-03-21T11:14:00.657256+00:00",
                      "end_time": "2024-03-21T11:14:00.657639+00:00",
                      "parent_span_id": "1c04bf28-8c29-42b1-9530-c8836f692806",
                      "inputs": "{'query': 'What did the president say about Ketanji Brown Jackson'}",
                      "outputs": "{'chunks': [{'chunk_id': null, 'doc_uri': null, 'content': 'And I will keep doing everything in my power'}]}",
                      "attributes": "{}",
                      "events": [
                        {"name": "start", "timestamp": "2024-03-21T11:14:00.657256+00:00", "attributes": "{}"},
                        {"name": "end", "timestamp": "2024-03-21T11:14:00.657639+00:00", "attributes": "{}"}
                      ]
                    },
                    {
                      "name": "AzureOpenAI",
                      "context": {"request_id": "", "span_id": "88b17f8b-03bf-4bcf-941d-702fca938c20"},
                      "status": {"status_code": "OK", "description": ""},
                      "span_type": "LLM",
                      "start_time": "2024-03-21T11:14:00.671217+00:00",
                      "end_time": "2024-03-21T11:14:02.901256+00:00",
                      "parent_span_id": "e19ea05e-df4f-449f-a0f7-461f6327456b",
                      "inputs": "{'prompt': 'Use the following pieces of context to answer the question at the end.Answer:'}",
                      "outputs": "{'generated_text': 'Nothing in these pieces of context mentions her. '}",
                      "attributes": "{'invocation_params': {'deployment_name': 'gpt-35-turbo', 'model_name': 'gpt-3.5-turbo-instruct', 'temperature': 0.7, 'top_p': 1, 'frequency_penalty': 0, 'presence_penalty': 0, 'n': 1, 'logit_bias': {}, 'max_tokens': 256, '_type': 'azure', 'stop': null}, 'options': {'stop': null}, 'batch_size': 1}",
                      "events": [
                        {"name": "start", "timestamp": "2024-03-21T11:14:00.671217+00:00", "attributes": "{}"},
                        {"name": "end", "timestamp": "2024-03-21T11:14:02.901256+00:00", "attributes": "{}"}
                      ]
                    }
                  ]
                }
              }
            }
            """


@pytest.mark.edge_spark
def test_unpack_and_split_payloads_trace_v2(
    spark, sample_requests, sample_rag_response_v2, monkeypatch
):
    monkeypatch.setenv("RAG_TRACE_V2_ENABLED", "true")
    payloads = sample_payload_logs(spark, sample_requests, sample_rag_response_v2)
    request_log, assessment_log = unpack_and_split_payloads(payloads)

    # Check that the schema of the resulting DataFrames is correct
    assert schemas_equal(request_log.schema, REQUEST_LOG_V2_SCHEMA)
    assert schemas_equal(assessment_log.schema, ASSESSMENT_LOG_SCHEMA)

    # Check the row counts for the resulting DataFrames
    # We have 5 payloads in the sample data, but 1 is an erroneous request that will be filtered out
    # The request payload results in 1 row
    # The text assessment payload results in 1 row +
    # The retrieval assessment payload results in 2 rows +
    # The combined assessment payload results in 3 more rows (1 text + 2 retrieval)
    expected_request_log_count = 1
    expected_assessment_log_count = 1 + 2 + (1 + 2)
    request_log_count = request_log.count()
    assessment_log_count = assessment_log.count()
    assert (
        request_log_count == expected_request_log_count
    ), f"expected {expected_request_log_count} rows, got {request_log_count}"
    assert (
        assessment_log_count == expected_assessment_log_count
    ), f"expected {expected_assessment_log_count} rows, got {assessment_log_count}"

    # Spot check a few values in the request log
    request_log_values = request_log.collect()[0].asDict()
    assert request_log_values["request"]["last_input"] == "Is mlflow good?"
    assert (
        request_log_values["trace"]["spans"][0]["inputs"]
        == "{'query': 'What did the president say about Ketanji Brown Jackson'}"
    )
    assert (
        request_log_values["output"]["choices"][0]["message"]["content"]
        == "MLflow is amazing!"
    )

    # Spot check a few values in the assessment log
    assessment_log_values = assessment_log.collect()[0].asDict()
    assert (
        assessment_log_values["text_assessment"]["ratings"]["harmful"]["rationale"]
        == "too mean"
    )
    assert assessment_log_values["retrieval_assessment"] is None
