import datetime
import os
import shutil
import tempfile
from unittest import mock

import pandas as pd
import pytest
from pyspark.sql import types as T

from databricks.rag.evaluation import online
from databricks.rag.unpacking.schemas import (
    ASSESSMENT_LOG_SCHEMA,
)
from databricks.sdk.service.serving import (
    AutoCaptureConfigOutput,
    AutoCaptureState,
    EndpointCoreConfigOutput,
    PayloadTable,
    ServingEndpointDetailed,
)

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
def sample_assessment_log(spark):
    assessment_data = [
        # The "basic" assessment row
        {
            "request_id": "123456",
            "step_id": None,
            "source": {
                "type": "llm judge",
                "id": "endpoints:/databricks-llama-2-70b-chat",
                "tags": {},
            },
            "timestamp": datetime.datetime(2023, 1, 9, 0, 0, 0),
            "text_assessment": {
                "step_id": None,
                "ratings": {
                    "faithful": {
                        "bool_value": True,
                        "rationale": "foo",
                    }
                },
            },
            "retrieval_assessment": None,
        },
        # A duplicate of the basic assessment row but 2 hours later
        {
            "request_id": "123456",
            "step_id": None,
            "source": {
                "type": "llm judge",
                "id": "endpoints:/databricks-llama-2-70b-chat",
                "tags": {},
            },
            "timestamp": datetime.datetime(2023, 1, 9, 2, 0, 0),
            "text_assessment": {
                "step_id": None,
                "ratings": {
                    "faithful": {
                        "bool_value": True,
                        "rationale": "foo",
                    }
                },
            },
            "retrieval_assessment": None,
        },
        # The basic row but with a different judge
        {
            "request_id": "123456",
            "step_id": None,
            "source": {
                "type": "expert",
                "id": "prithvish",
                "tags": {},
            },
            "timestamp": datetime.datetime(2023, 1, 9, 0, 0, 0),
            "text_assessment": {
                "step_id": None,
                "ratings": {
                    "faithful": {
                        "bool_value": True,
                        "rationale": "foo",
                    }
                },
            },
            "retrieval_assessment": None,
        },
        # A retrieval assessment for the same request
        {
            "request_id": "123456",
            "step_id": "098765",
            "source": {
                "type": "expert",
                "id": "prithvish",
                "tags": {},
            },
            "timestamp": datetime.datetime(2023, 1, 9, 11, 22, 33),
            "text_assessment": None,
            "retrieval_assessment": {
                "step_id": "098765",
                "position": 1,
                "ratings": {
                    "relevant": {
                        "bool_value": False,
                        "rationale": "super irrelevant",
                    }
                },
            },
        },
        # An identical retrieval assessment (including chunk position) but with a later timestamp
        {
            "request_id": "123456",
            "step_id": "098765",
            "source": {
                "type": "expert",
                "id": "prithvish",
                "tags": {},
            },
            "timestamp": datetime.datetime(2023, 1, 9, 11, 23, 33),
            "text_assessment": None,
            "retrieval_assessment": {
                "step_id": "098765",
                "position": 1,
                "ratings": {
                    "relevant": {
                        "bool_value": False,
                        "rationale": "super irrelevant",
                    }
                },
            },
        },
    ]

    return spark.createDataFrame(
        pd.DataFrame(assessment_data), schema=ASSESSMENT_LOG_SCHEMA
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


@pytest.fixture()
def streaming_checkpoint_dir():
    checkpoint_dir = tempfile.mkdtemp()
    yield checkpoint_dir

    if os.path.exists(checkpoint_dir) and os.path.isdir(checkpoint_dir):
        shutil.rmtree(checkpoint_dir)


@mock.patch("databricks.sdk.WorkspaceClient", autospec=True)
def test_get_payload_table_name(MockWorkspaceClient):
    """Tests that we can get the payload table name from an endpoint name."""
    MockWorkspaceClient.return_value.serving_endpoints.get.return_value = (
        ServingEndpointDetailed(
            config=EndpointCoreConfigOutput(
                auto_capture_config=AutoCaptureConfigOutput(
                    catalog_name="my_cat",
                    schema_name="my_dog",
                    state=AutoCaptureState(
                        payload_table=PayloadTable(
                            name="my_tab",
                        )
                    ),
                )
            )
        )
    )
    assert online.get_payload_table_name("my_endpoint") == "`my_cat`.`my_dog`.`my_tab`"


def test_dedup_assessment_logs(sample_assessment_log):
    """Tests that we can dedup assessments correctly"""
    # We have 5 rows in the assessment log, but 2 of them are duplicates with a later timestamp
    deduped = online.dedup_assessment_logs(sample_assessment_log)
    assert deduped.count() == 5 - 2
    # Check that the schema is unchanged
    assert sample_assessment_log.schema == deduped.schema


def test_dedup_assessment_logs_by_hour(sample_assessment_log):
    """Tests that we can dedup assessments by the hour window."""
    # We have 5 rows in the assessment log, 2 are duplicates, but 1 duplicate's
    # later timestamp should prevent it from being filtered out.
    deduped = online.dedup_assessment_logs(sample_assessment_log, "hour")
    assert deduped.count() == 4
    # Check that the schema is unchanged
    assert sample_assessment_log.schema == deduped.schema


def test_dedup_assessment_logs_invalid_granularity(sample_assessment_log):
    """Tests that we raise an error if the granularity is invalid."""
    with pytest.raises(ValueError, match="granularity must be one of .*"):
        online.dedup_assessment_logs(sample_assessment_log, "day")


def test_persist_stream(spark, streaming_checkpoint_dir):
    """Tests that we can initialize and write streaming jobs to Delta tables."""
    _SRC_TABLE_NAME = "test_src_table"
    _SINK_TABLE_NAME = "test_sink_table"

    # Initialize some data that we can read in as a stream
    data = [(1, "Alice"), (2, "Bob"), (3, "Charlie")]
    columns = ["id", "name"]
    df = spark.createDataFrame(data, columns)
    df.write.format("delta").mode("overwrite").saveAsTable(_SRC_TABLE_NAME)

    stream_df = spark.readStream.format("delta").table(_SRC_TABLE_NAME)
    online.persist_stream(_SINK_TABLE_NAME, stream_df, streaming_checkpoint_dir)

    # Read the persisted stream back in and check that it's the same as the original data
    persisted_df = spark.read.format("delta").table(_SINK_TABLE_NAME)
    assert persisted_df.schema == stream_df.schema
    persisted_pdf = persisted_df.toPandas()
    assert len(persisted_pdf) == len(data)
    assert set(persisted_pdf["name"]) == {"Alice", "Bob", "Charlie"}

    # Make sure the CDF and column mapping was enabled on the sink table
    details = spark.sql(f"DESCRIBE DETAIL {_SINK_TABLE_NAME}").collect()[0].asDict()
    assert details["properties"]["delta.enableChangeDataFeed"] == "true"
    assert details["properties"]["delta.columnMapping.mode"] == "name"

    # Write more streaming data to the sink table to make sure the checkpointing works
    data_2 = [(4, "Alkis"), (5, "Vish"), (6, "Prithvi")]
    df_2 = spark.createDataFrame(data_2, columns)
    df_2.write.format("delta").mode("append").saveAsTable(_SRC_TABLE_NAME)
    stream_df_2 = spark.readStream.format("delta").table(_SRC_TABLE_NAME)

    online.persist_stream(_SINK_TABLE_NAME, stream_df_2, streaming_checkpoint_dir)
    persisted_df_2 = spark.read.format("delta").table(_SINK_TABLE_NAME)
    persisted_pdf_2 = persisted_df_2.toPandas()
    assert len(persisted_pdf_2) == len(data) * 2  # 2x the original data
    assert sorted(persisted_pdf_2["id"]) == [1, 2, 3, 4, 5, 6]
