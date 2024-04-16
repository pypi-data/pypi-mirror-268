from enum import Enum
class DataSourceMaster:
    TEXT = "TEXT"
    PDF = "PDF"
    WEBSITE = "WEBSITE"
    DOCX = "DOCX"
    CSV = "CSV"
    DATABASE = "DATABASE"
    YOUTUBE="YOUTUBE"

class EmbeddingModelMaster:
    OPENAI_TEXT_ADA = 'text-embedding-ada-002'
    OPENAI_TEXT_EMBEDDING_3_LARGE = 'text-embedding-3-large'
    OPENAI_TEXT_EMBEDDING_3_SMALL = 'text-embedding-3-small'
    AZURE_TEXT_ADA='text-embedding-ada-002'
    AZURE_TEXT_EMBEDDING_3_LARGE = 'text-embedding-3-large'
    AZURE_TEXT_EMBEDDING_3_SMALL = 'text-embedding-3-small'
    BEDROCK_TITAN_EMBEDDING='amazon.titan-embed-text-v1'
    BEDROCK_TITAN_MULTIMODAL_EMBEDDING='amazon.titan-embed-image-v1'

class InferenceModelMaster:
    OPENAI_GPT_4_TURBO_PREVIEW = 'gpt-4-turbo-preview'
    OPENAI_GPT_4 = 'gpt-4'
    OPENAI_GPT_3_5_TURBO = 'gpt-3.5-turbo'
    OPENAI_GPT_3_5_TURBO_INSTRUCT = 'gpt-3.5-turbo-instruct'
    AZURE_GPT_4_TURBO_PREVIEW = 'gpt-4-turbo-preview'
    AZURE_GPT_4 = 'gpt-4'
    AZURE_GPT_3_5_TURBO = 'gpt-3.5-turbo'
    AZURE_GPT_3_5_TURBO_INSTRUCT = 'gpt-3.5-turbo-instruct'
    GROQ_LLM_MIXTRAL_8_7_B='mixtral-8x7b-32768'
    GROQ_LLM_LLAMA2_70B= 'llama2-70b-4096'
    GROQ_LLM_GEMMA7B= 'gemma-7b-it'
    BEDROCK_TEXT_EXPRES_V1='amazon.titan-text-express-v1'
    BEDROCK_TEXT_LITE_G1='amazon.titan-text-lite-v1'

class OutputSourceMaster:
    S3 = "S3"
    LOCAL = "LOCAL"
    DATABASE = "DATABASE"


class ChatMessage(Enum):
    CHAT_SAVED = "Message saved successfully!"
    CHAT_FAILED = "Error saving message"
    FAILED_TO_RETRIEVE = "Error retrieving message history"
