from pyspark.sql import types as T


######################################################################
# Request log schema definitions
######################################################################

# Format of the conversation following the OpenAI messages format.
MESSAGE_SCHEMA = T.StructType(
    [
        T.StructField("role", T.StringType()),
        T.StructField("content", T.StringType()),
    ]
)

# Format of the RAG response in the choices format.
CHOICES_SCHEMA = T.ArrayType(T.StructType([T.StructField("message", MESSAGE_SCHEMA)]))

# Schema of a single retrieval chunk in the trace step.
CHUNK_SCHEMA = T.StructType(
    [
        T.StructField("chunk_id", T.StringType()),
        T.StructField("doc_uri", T.StringType()),
        T.StructField("content", T.StringType()),
    ]
)

RETRIEVAL_SCHEMA = T.StructType(
    [
        T.StructField("query_text", T.StringType()),
        T.StructField("chunks", T.ArrayType(CHUNK_SCHEMA)),
    ]
)

TEXT_GENERATION_SCHEMA = T.StructType(
    [
        T.StructField("prompt", T.StringType()),
        T.StructField("generated_text", T.StringType()),
    ]
)

# Schema for an individual trace step.
TRACE_STEP_SCHEMA = T.StructType(
    [
        T.StructField("step_id", T.StringType()),
        T.StructField("name", T.StringType()),
        T.StructField("type", T.StringType()),
        T.StructField("start_timestamp", T.TimestampType()),
        T.StructField("end_timestamp", T.TimestampType()),
        T.StructField("retrieval", RETRIEVAL_SCHEMA),
        T.StructField("text_generation", TEXT_GENERATION_SCHEMA),
    ]
)

# Schema of the "trace" field in the final request logs table.
TRACE_SCHEMA = T.StructType(
    [
        T.StructField("app_version_id", T.StringType()),
        T.StructField("start_timestamp", T.TimestampType()),
        T.StructField("end_timestamp", T.TimestampType()),
        T.StructField("is_truncated", T.BooleanType()),
        T.StructField("steps", T.ArrayType(TRACE_STEP_SCHEMA)),
    ]
)

MESSAGES_SCHEMA = T.ArrayType(MESSAGE_SCHEMA)

REQUEST_SCHEMA = T.StructType(
    [
        T.StructField("request_id", T.StringType()),
        T.StructField("conversation_id", T.StringType()),
        T.StructField("timestamp", T.TimestampType()),
        T.StructField("messages", MESSAGES_SCHEMA),
        T.StructField("last_input", T.StringType()),
    ]
)

# Full schema of the final request logs table.
REQUEST_LOG_SCHEMA = T.StructType(
    [
        T.StructField("request", REQUEST_SCHEMA),
        T.StructField("trace", TRACE_SCHEMA),
        T.StructField(
            "output", T.StructType([T.StructField("choices", CHOICES_SCHEMA)])
        ),
    ]
)
