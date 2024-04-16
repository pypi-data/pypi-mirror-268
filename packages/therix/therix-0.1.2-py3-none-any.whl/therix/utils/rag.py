import json
from operator import itemgetter
from pathlib import Path
from langchain.docstore.document import Document
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores.pgvector import PGVector
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_openai import AzureOpenAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureOpenAIEmbeddings

from therix.core.JSONLoader import JSONLoader
from langchain_community.embeddings import BedrockEmbeddings
import boto3
from langchain_community.llms import Bedrock
from therix.core.constants import (
    DataSourceMaster,
    EmbeddingModelMaster,
    InferenceModelMaster,
)
from therix.db.session import SQLALCHEMY_DATABASE_URL
from langfuse.callback import CallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores.pgvector import PGVector
from langchain.memory import PostgresChatMessageHistory
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import get_buffer_string
from langchain_core.prompts import format_document
from langchain_core.runnables import RunnableParallel
from operator import itemgetter


def sanitize_text(text):
    # Remove null characters (0x00) from the text
    sanitized_text = text.replace("\x00", "")
    return sanitized_text


def get_loader(file_type, file_path, config):
    if file_type == DataSourceMaster.TEXT:
        return TextLoader(file_path)
    elif file_type == DataSourceMaster.PDF:
        return PyPDFLoader(file_path)
    elif file_type == DataSourceMaster.YOUTUBE:
        return YoutubeLoader.from_youtube_url(
            file_path,
            add_video_info=True,
            language=[config["language"], "id"],
            translation="en",
        )
        return PyPDFLoader(file_path)
    elif file_type == DataSourceMaster.WEBSITE:
        return JSONLoader(file_path)
    else:
        raise ValueError(f"Unknown data source type: {file_type}")


def get_embedding_model(embedding_model_name, config):
    print(embedding_model_name, config)
    if (
        embedding_model_name == EmbeddingModelMaster.OPENAI_TEXT_ADA
        or embedding_model_name == EmbeddingModelMaster.OPENAI_TEXT_EMBEDDING_3_SMALL
        or embedding_model_name == EmbeddingModelMaster.OPENAI_TEXT_EMBEDDING_3_LARGE
    ) and ("api_key" in config):
        return OpenAIEmbeddings(
            openai_api_key=config["api_key"], model=embedding_model_name
        )
    elif (
        embedding_model_name == EmbeddingModelMaster.AZURE_TEXT_ADA
        or embedding_model_name == EmbeddingModelMaster.AZURE_TEXT_EMBEDDING_3_LARGE
        or embedding_model_name == EmbeddingModelMaster.AZURE_TEXT_EMBEDDING_3_SMALL
    ) and ("azure_api_key" in config):
        return AzureOpenAIEmbeddings(
            api_key=config["azure_api_key"],
            model=embedding_model_name,
            azure_endpoint=config["azure_endpoint"],
            openai_api_version=config["openai_api_version"],
            azure_deployment=config["azure_deployment"],
        )

    elif (
        embedding_model_name == EmbeddingModelMaster.BEDROCK_TITAN_EMBEDDING
        or embedding_model_name
        == EmbeddingModelMaster.BEDROCK_TITAN_MULTIMODAL_EMBEDDING
    ) and ("bedrock_aws_session_token" in config):
        bedrock_client = boto3.client(
            service_name="bedrock-runtime",
            aws_access_key_id=config["bedrock_aws_access_key_id"],
            aws_secret_access_key=config["bedrock_aws_secret_access_key"],
            aws_session_token=config["bedrock_aws_session_token"],
            region_name=config["bedrock_region_name"],
        )

        return BedrockEmbeddings(
            credentials_profile_name="bedrock-admin",
            client=bedrock_client,
            model_id=embedding_model_name,
            region_name=config["bedrock_region_name"],
        )
    else:
        raise ValueError(f"Unknown embedding model: {embedding_model_name}")


def get_inference_model(inference_model_name, config):
    if (
        inference_model_name == InferenceModelMaster.OPENAI_GPT_3_5_TURBO
        or inference_model_name == InferenceModelMaster.OPENAI_GPT_3_5_TURBO_INSTRUCT
        or inference_model_name == InferenceModelMaster.OPENAI_GPT_4
        or inference_model_name == InferenceModelMaster.OPENAI_GPT_4_TURBO_PREVIEW
    ) and ("api_key" in config):
        return ChatOpenAI(openai_api_key=config["api_key"], model=inference_model_name)
    elif (
        inference_model_name == InferenceModelMaster.OPENAI_GPT_3_5_TURBO
        or inference_model_name == InferenceModelMaster.OPENAI_GPT_3_5_TURBO_INSTRUCT
        or inference_model_name == InferenceModelMaster.OPENAI_GPT_4
        or inference_model_name == InferenceModelMaster.OPENAI_GPT_4_TURBO_PREVIEW
    ) and ("azure_api_key" in config):
        return AzureOpenAI(
            api_key=config["azure_api_key"],
            model=inference_model_name,
            deployment_name=config["deployment_name"],
            azure_endpoint=config["azure_endpoint"],
            api_version=config["openai_api_version"],
        )
    elif (
        inference_model_name == InferenceModelMaster.GROQ_LLM_MIXTRAL_8_7_B
        or inference_model_name == InferenceModelMaster.GROQ_LLM_LLAMA2_70B
        or inference_model_name == InferenceModelMaster.GROQ_LLM_GEMMA7B
    ) and ("groq_api_key" in config):
        return ChatGroq(groq_api_key=config["groq_api_key"], model=inference_model_name)

    elif (
        inference_model_name == InferenceModelMaster.BEDROCK_TEXT_EXPRES_V1
        or inference_model_name == InferenceModelMaster.BEDROCK_TEXT_LITE_G1
    ) and ("bedrock_aws_session_token" in config):
        bedrock_client = boto3.client(
            service_name="bedrock-runtime",
            aws_access_key_id=config["bedrock_aws_access_key_id"],
            aws_secret_access_key=config["bedrock_aws_secret_access_key"],
            aws_session_token=config["bedrock_aws_session_token"],
            region_name=config["bedrock_region_name"],
        )
        return Bedrock(
            credentials_profile_name="bedrock-admin",
            model_id=inference_model_name,
            client=bedrock_client,
            region_name=config["bedrock_region_name"],
        )
    else:
        raise ValueError(f"Unknown inference model: {inference_model_name}")


def create_embeddings(data_sources, embedding_model, collection_name):
    store = get_vectorstore(embedding_model, collection_name)
    for data_source in data_sources:
        # data_source = {'name': 'PDF', 'config': {'files': ['path/to/file', 'path/to/file']}}
        for file_path in data_source.config["files"]:
            loader = get_loader(data_source.name, file_path, data_source.config)
            pages = loader.load_and_split()
            # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

            store.add_documents(pages)
            return "embedding created"


def get_vectorstore(embedding_model, collection_name):
    embeddings = get_embedding_model(embedding_model.name, embedding_model.config)
    store = PGVector(
        collection_name=collection_name,
        connection_string=SQLALCHEMY_DATABASE_URL,
        embedding_function=embeddings,
    )
    return store


def chat(
    question,
    retriever,
    inference_model,
    embed_model,
    session_id,
    pipeline_id,
    trace_details=None,
):

    print(trace_details)

    chain_callbacks = []
    if trace_details is not None:
        langfuse_handler = CallbackHandler(
            secret_key=trace_details["secret_key"],
            public_key=trace_details["public_key"],
            host=trace_details["host"],
            trace_name=trace_details["identifier"],
        )
        chain_callbacks.append(langfuse_handler)

    history = PostgresChatMessageHistory(
        connection_string=SQLALCHEMY_DATABASE_URL,
        table_name="chat_history",
        session_id=str(session_id),
    )
    chat_history = history.messages

    template = """Answer the question based only on the following context:
                     {context}

                    Question: {question}
                    """
    ANSWER_PROMPT = ChatPromptTemplate.from_template(template)
    _template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.
                    Chat History:
                    {chat_history}
                    Follow Up Input: {question}
                    Standalone question:"""

    CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)
    DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")

    def _combine_documents(
        docs, document_prompt=DEFAULT_DOCUMENT_PROMPT, document_separator="\n\n"
    ):
        doc_strings = [format_document(doc, document_prompt) for doc in docs]
        return document_separator.join(doc_strings)

    model = get_inference_model(inference_model.name, inference_model.config)

    _inputs = RunnableParallel(
        standalone_question=RunnablePassthrough.assign(
            chat_history=lambda x: get_buffer_string(x["chat_history"])
        )
        | CONDENSE_QUESTION_PROMPT
        | model
        | StrOutputParser(),
    )
    _context = {
        "context": itemgetter("standalone_question") | retriever | _combine_documents,
        "question": lambda x: x["standalone_question"],
    }
    conversational_qa_chain = _inputs | _context | ANSWER_PROMPT | model
    result = conversational_qa_chain.invoke(
        {"question": question, "chat_history": chat_history}
    )

    history.add_user_message(question)
    history.add_ai_message(result)
    return json.loads(result.json())["content"]
