from enum import Enum


class SpanAttributes:
    # LLM
    LLM_VENDOR = "llm.vendor"
    LLM_REQUEST_TYPE = "llm.request.type"
    LLM_REQUEST_MODEL = "llm.request.model"
    LLM_RESPONSE_MODEL = "llm.response.model"
    LLM_REQUEST_MAX_TOKENS = "llm.request.max_tokens"
    LLM_USAGE_TOTAL_TOKENS = "llm.usage.total_tokens"
    LLM_USAGE_COMPLETION_TOKENS = "llm.usage.completion_tokens"
    LLM_USAGE_PROMPT_TOKENS = "llm.usage.prompt_tokens"
    LLM_TEMPERATURE = "llm.temperature"
    LLM_USER = "llm.user"
    LLM_HEADERS = "llm.headers"
    LLM_TOP_P = "llm.top_p"
    LLM_TOP_K = "llm.top_k"
    LLM_IS_STREAMING = "llm.is_streaming"
    LLM_FREQUENCY_PENALTY = "llm.frequency_penalty"
    LLM_PRESENCE_PENALTY = "llm.presence_penalty"
    LLM_PROMPTS = "llm.prompts"
    LLM_COMPLETIONS = "llm.completions"
    LLM_CHAT_STOP_SEQUENCES = "llm.chat.stop_sequences"
    LLM_REQUEST_FUNCTIONS = "llm.request.functions"

    # Vector DB
    VECTOR_DB_VENDOR = "db.system"
    VECTOR_DB_QUERY_TOP_K = "db.vector.query.top_k"

    # LLM Workflows
    SYNTRAC_SPAN_KIND = "syntrac.span.kind"
    SYNTRAC_WORKFLOW_NAME = "syntrac.workflow.name"
    SYNTRAC_ENTITY_NAME = "syntrac.entity.name"
    SYNTRAC_ENTITY_INPUT = "syntrac.entity.input"
    SYNTRAC_ENTITY_OUTPUT = "syntrac.entity.output"
    SYNTRAC_ASSOCIATION_PROPERTIES = "syntrac.association.properties"

    # Deprecated
    SYNTRAC_CORRELATION_ID = "syntrac.correlation.id"

    # Watson/genai LLM
    LLM_DECODING_METHOD = "llm.watsonx.decoding_method"
    LLM_RANDOM_SEED = "llm.watsonx.random_seed"
    LLM_MAX_NEW_TOKENS = "llm.watsonx.max_new_tokens"
    LLM_MIN_NEW_TOKENS = "llm.watsonx.min_new_tokens"
    LLM_REPETITION_PENALTY = "llm.watsonx.repetition_penalty"


class Events(Enum):
    DB_QUERY_EMBEDDINGS = "db.query.embeddings"
    DB_QUERY_RESULT = "db.query.result"


class EventAttributes(Enum):
    # Query Embeddings
    DB_QUERY_EMBEDDINGS_VECTOR = "db.query.embeddings.vector"

    # Query Result (canonical format)
    DB_QUERY_RESULT_ID = "db.query.result.id"
    DB_QUERY_RESULT_SCORE = "db.query.result.score"
    DB_QUERY_RESULT_DISTANCE = "db.query.result.distance"
    DB_QUERY_RESULT_METADATA = "db.query.result.metadata"
    DB_QUERY_RESULT_VECTOR = "db.query.result.vector"
    DB_QUERY_RESULT_DOCUMENT = "db.query.result.document"


class LLMRequestTypeValues(Enum):
    COMPLETION = "completion"
    CHAT = "chat"
    RERANK = "rerank"
    EMBEDDING = "embedding"
    UNKNOWN = "unknown"


class SyntracSpanKindValues(Enum):
    WORKFLOW = "workflow"
    TASK = "task"
    AGENT = "agent"
    TOOL = "tool"
    UNKNOWN = "unknown"
