"""
    :param FileName     :   test_data_models.py
    :param Author       :   Sudo
    :param Date         :   02/1/2024
    :param Copyright    :   Copyright (c) 2024 Ryght, Inc. All Rights Reserved.
    :param License      :   # TODO
    :param Description  :   # TODO
"""
import importlib.util
# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Import section |--->
# -------------------------------------------------------------------------------------------------------------------- #
import yaml
import logging

from typing import Any, Optional
from datetime import datetime, timedelta
from pydantic import BaseModel, ConfigDict, model_validator, Field

# -------------------------------------------------------------------------------------------------------------------- #
logger = logging.getLogger(__name__)


# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Class Definition |--->
# -------------------------------------------------------------------------------------------------------------------- #
class Token(BaseModel):
    """
    A data class that holds authorization token information
    """
    model_config = ConfigDict(extra='ignore')

    token_type: str | None
    expires_in: int | None
    access_token: str | None
    refresh_token: str | None
    refresh_expires_in: int | None
    token_expiry: datetime
    refresh_expiry: datetime

    @property
    def authorization_param(self) -> str:
        return (lambda: self.token_type + ' ' + self.access_token)()

    @staticmethod
    def init_as_none():
        return Token(
            **{
                'token_type': None,
                'expires_in': 5,
                'access_token': None,
                'refresh_token': None,
                'refresh_expires_in': 5
            }
        )

    @model_validator(mode='before')
    @classmethod
    def compute_expiration(cls, params: Any) -> Any:
        """

        :param params:
        :return:
        """
        assert 'expires_in' and 'refresh_expires_in' in params
        params['token_expiry'], params['refresh_expiry'] = Token.set_expiration(
            expires_in=params['expires_in'],
            refresh_expires_in=params['refresh_expires_in']
        )
        return params

    @staticmethod
    def set_expiration(expires_in: int, refresh_expires_in: int) -> tuple:
        """

        :param expires_in:
        :param refresh_expires_in:
        :return:
        """
        now = datetime.utcnow()
        return now + timedelta(seconds=expires_in), now + timedelta(seconds=refresh_expires_in)


# -------------------------------------------------------------------------------------------------------------------- #

class Collection(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    name: str
    tags: list
    states: list
    documents_count: int | str
    default: bool = False
    embedding_models: list

    @model_validator(mode='before')
    @classmethod
    def transform_data(cls, params: Any) -> Any:
        """

        :param params:
        :return:
        """
        if 'embeddingModels' in params:
            params['embedding_models'] = Collection.extract_embedding_models_details(params['embeddingModels'])
        if 'documentsCount' in params:
            params['documents_count'] = params['documentsCount']
        return params

    @staticmethod
    def extract_embedding_models_details(embedding_models_list: list) -> list:
        embedding_models = []
        for model_info in embedding_models_list:
            embedding_models.append(AIModels(**model_info))
        return embedding_models


# -------------------------------------------------------------------------------------------------------------------- #

class CompletionsResponse(BaseModel):
    model_config = ConfigDict(extra='ignore')

    answer: str | None
    embeddings: list | None

    @model_validator(mode='before')
    @classmethod
    def transform_data(cls, params: Any) -> Any:
        """

        :param params:
        :return:
        """
        if 'embeddings' not in params:
            params['embeddings'] = None
        if 'answer' not in params:
            params['answer'] = None
        return params

    @staticmethod
    def init_with_none():
        return CompletionsResponse(**{'answer': None, 'embeddings': None})


# -------------------------------------------------------------------------------------------------------------------- #

class TraceStatus(BaseModel):
    model_config = ConfigDict(extra='ignore')

    status: str
    message: str


# -------------------------------------------------------------------------------------------------------------------- #

class AIModels(BaseModel):
    model_config = ConfigDict(extra='allow')
    id: str
    name: str
    provider: str
    default: bool = False

    # Optional Fields
    tags: str | None
    description: str | None


# -------------------------------------------------------------------------------------------------------------------- #

class Documents(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    name: str
    states: Optional[list[str]] = None
    content: Optional[str] = None


# -------------------------------------------------------------------------------------------------------------------- #
class ChunkedDocumentsMetadata(BaseModel):
    model_config = ConfigDict(extra='allow')

    doi: str = Field(
        ...,
        description='URL or path to view the document online'
    )
    source_path: str = Field(
        ...,
        alias='source',
        description='The url or link to the location where the document can be retrieved'
    )
    extra_fields: dict = Field(
        ...,
        alias='extraFields',
        description='Store extra information relevant to chunked document in here'
    )


# -------------------------------------------------------------------------------------------------------------------- #
class ChunkedDocumentsCollectionsMetadata(BaseModel):
    model_config = ConfigDict(extra='ignore')

    source: str = Field(
        ...,
        description='From whom/where the collection is sourced from'
    )
    extra_fields: dict = Field(
        ...,
        alias='extraFields',
        description='Store extra information relevant to collection in here'
    )


# -------------------------------------------------------------------------------------------------------------------- #
class ChunksOfDocumentContent(BaseModel):
    model_config = ConfigDict(extra='ignore')

    content: str = Field(
        ...,
        description='chunk of a given document'
    ),
    order: int = Field(
        ...,
        ge=-1,
        description='order of the chunk within a document',
    ),
    extra_fields: dict = Field(
        ...,
        alias='extraFields',
        description='Other extra information relevant to the chunk and its specification goes here'
    )


# -------------------------------------------------------------------------------------------------------------------- #

class JsonDocument(BaseModel):
    model_config = ConfigDict(extra='ignore')

    name: str = Field(
        ...,
        description='Name of the document'
    ),
    content: str = Field(
        ...,
        description="Whole content of the document that's been chunked"
    ),
    metadata: ChunkedDocumentsMetadata = Field(
        ...,
        description='Metadata about the document'
    )


# -------------------------------------------------------------------------------------------------------------------- #
class ChunkedDocument(JsonDocument):
    chunks: list[ChunksOfDocumentContent] = Field(
        ...,
        description='List of chunks of a given document'
    )


# -------------------------------------------------------------------------------------------------------------------- #

class ChunkedDocumentCollection(BaseModel):
    model_config = ConfigDict(extra='ignore')

    collection_name: str = Field(
        ...,
        description='Name of the collection the docs belongs to',
        alias='collectionName'
    )
    chunk_specification: dict = Field(
        default={
            "name": "EXTERNAL_SPECIFICATION",
            "description": "Custom chunk description"
        },
        description='Chunk specification for the chunked documents, by default its set to External Specification',
        alias='chunkSpecification')
    metadata: ChunkedDocumentsCollectionsMetadata = Field(
        ...,
        description='Metadata about the collection'
    )

    documents: list[ChunkedDocument] = Field(
        ...,
        description='List of chunked Documents'
    )


# -------------------------------------------------------------------------------------------------------------------- #
class ConversationResponseCollection(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str = Field(
        ...,
        description='collection id'
    )
    name: str = Field(
        ...,
        description='collection name'
    )


# -------------------------------------------------------------------------------------------------------------------- #
class ConversationResponseDocuments(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str = Field(
        ...,
        description='collection id'
    )
    name: str = Field(
        ...,
        description='collection name'
    )


# -------------------------------------------------------------------------------------------------------------------- #
class ConversationResponseEmbeddings(BaseModel):
    model_config = ConfigDict(extra='ignore')

    content: str = Field(
        ...,
        description='Content of the embeddings that matched'
    )
    cosine_distance: str = Field(
        ...,
        description='distance score of the embeddings',
        alias='cosineDistance'
    )
    document: dict = Field(
        ...,
        description='document of the embeddings'
    )


# -------------------------------------------------------------------------------------------------------------------- #
class ConversationResponse(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str = Field(
        ...,
        description='Conversation ID'
    )
    question: str = Field(
        ...,
        description='Question Asked.'
    )
    answer: str = Field(
        ...,
        description='Answer we got from the conversation service'
    )
    created_at: str = Field(
        ...,
        description='time the conversation was created',
        alias='createdAt'
    )

    collections: list[ConversationResponseCollection] = Field(
        [],
        description='List of collections the conversation is based on'
    )

    documents: list[ConversationResponseDocuments] = Field(
        [],
        description='List of documents the conversation is based on'
    )
    embeddings: list[ConversationResponseEmbeddings] = Field(
        [],
        description='List of embeddings the conversation depends on '
    )

    @model_validator(mode='before')
    @classmethod
    def parse_input_data(cls, params: Any) -> Any:
        if 'collections' in params:
            params['collections'] = ConversationResponse.parse_collections(params['collections'])

        if 'documents' in params:
            params['documents'] = ConversationResponse.parse_documents(params['documents'])

        if 'embeddings' in params:
            params['embeddings'] = ConversationResponse.parse_embeddings(params['embeddings'])

        return params

    @staticmethod
    def parse_collections(collections_list: list[dict]) -> list[ConversationResponseCollection]:
        collections = []
        for collection_info in collections_list:
            collections.append(ConversationResponseCollection(**collection_info))
        return collections

    @staticmethod
    def parse_documents(documents_list: list[dict]) -> list[ConversationResponseDocuments]:
        documents = []
        for document_info in documents_list:
            documents.append(ConversationResponseDocuments(**document_info))
        return documents

    @staticmethod
    def parse_embeddings(embeddings_list: list[dict]) -> list[ConversationResponseEmbeddings]:
        embeddings = []
        for embedding_info in embeddings_list:
            embeddings.append(ConversationResponseEmbeddings(**embedding_info))
        return embeddings


# -------------------------------------------------------------------------------------------------------------------- #
class ConversationInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str = Field(
        ...,
        description='Conversation ID'
    )
    name: str = Field(
        ...,
        description='Conversation Name'
    )
    updated_at: str = Field(
        ...,
        description='last update time of the conversation',
        alias='updatedAt'
    )


# -------------------------------------------------------------------------------------------------------------------- #
class Prompts(BaseModel):
    model_config = ConfigDict(extra='ignore')

    template: str = Field(
        ...,
        description='Prompt templates'
    )
    keywords: dict = Field(
        ...,
        description='Conversation Name'
    )
# -------------------------------------------------------------------------------------------------------------------- #
