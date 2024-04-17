# <---| * Module Information |--->
# ==================================================================================================================== #
"""
    :param FileName     :   user.py
    :param Author       :   Sudo
    :param Date         :   2/02/2024
    :param Copyright    :   Copyright (c) 2024 Ryght, Inc. All Rights Reserved.
    :param License      :   #
    :param Description  :   #
"""
__author__ = 'Data engineering team'
__copyright__ = 'Copyright (c) 2024 Ryght, Inc. All Rights Reserved.'

# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Import section |--->
# -------------------------------------------------------------------------------------------------------------------- #
import json
import logging
import os.path
from urllib.parse import urljoin
from urllib.parse import urlencode

from ryght.utils import RequestMethods, FlowTypes, ModelOperation

from ryght.interface import (
    ApiInterface,
    Conversations
)

from ryght.models import (
    Collection,
    AIModels,
    Documents,
    TraceStatus,
    JsonDocument,
    CompletionsResponse,
    ChunkedDocumentCollection,
)

# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Logger Definition |--->
# -------------------------------------------------------------------------------------------------------------------- #
logger = logging.getLogger(__name__)


# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Class Definition |--->
# -------------------------------------------------------------------------------------------------------------------- #
class ApiClient(
    Conversations
):

    # Document Collections
    def get_collection_page_by_page(self, param: dict = None):
        raise NotImplementedError(f'Get collections page by page not implemented !')

    # Document Collection

    def create_new_collection(
            self,
            collection_name: str,
            metadata: dict | None = None,
            tag_ids: list | None = None
    ) -> str:
        logger.debug(f'Create a new/empty collection')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document_collection.base)
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        result = self.execute_request(
            method=RequestMethods.POST,
            url=url,
            headers=headers,
            data=json.dumps({
                'name': collection_name,
                'metadata': metadata,
                'tagIds': tag_ids if tag_ids else []
            })
        )
        return result.get('id')

    def get_all_available_collections(self) -> list[Collection]:
        return self.search_collections(
            query_params={
                'size': 100
            }
        )

    def search_collections(self, query_params: dict = None) -> list[Collection]:
        logger.debug(f'Getting available collections ...')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document_collection.search)
        if isinstance(query_params, dict):
            url = urljoin(url, '?' + urlencode(query_params))
            print(url)
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=self.get_headers(),
            timeout=10.0
        )
        collections = []
        if 'content' in result:
            for collection_details in result['content']:
                collections.append(Collection(**collection_details))
        return collections

    def get_collection_details(self, collection_id: str) -> Collection:
        logger.debug(f"Getting a collection's details ...")
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document_collection.by_id)
        url = url.format(id=collection_id)
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=self.get_headers()
        )

        return Collection(**result)

    def delete_collection_by_id(self, collection_id: str) -> str:
        logger.debug(f"Request a collection deletion by collection id ...")
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document_collection.by_id)
        url = url.format(id=collection_id)
        result: str = self.execute_request(
            method=RequestMethods.DELETE,
            url=url,
            headers=self.get_headers()
        )

        return result

    def upload_chunked_document_collection(self, document_collection: ChunkedDocumentCollection) -> str:
        logger.debug(f'Create/update chunked document collection')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document_collection.pre_chunked)
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        result = self.execute_request(
            method=RequestMethods.POST,
            url=url,
            headers=headers,
            data=document_collection.model_dump_json(by_alias=True)
        )
        return result

    def track_status(self, trace_id: str) -> TraceStatus:
        logger.debug(f'Tract status of a call using trace ID')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document_import.status)
        url = url.format(traceId=trace_id)
        headers = self.get_headers()
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=headers
        )
        return TraceStatus(**result)

    def upload_doc_as_json_to_a_document_collection(
            self,
            collection_id: str,
            document: JsonDocument
    ) -> str:
        logger.debug(f'Upload a doc to the document collection')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document_import.json_object)
        url = url.format(collectionId=collection_id)
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        result = self.execute_request(
            method=RequestMethods.POST,
            url=url,
            headers=headers,
            data=document.model_dump_json(by_alias=True)
        )
        return result

    def upload_pdf_doc_to_a_document_collection(
            self,
            collection_id: str,
            document_path: str,
            file_name: str
    ):
        logger.debug(f'Upload a PDF doc to the document collection')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document_import.pdf_file)
        url = url.format(collectionId=collection_id)
        headers = self.get_headers()
        data = {
            "fileName": file_name,
        }
        if os.path.isfile(document_path):
            with open(document_path, 'rb') as file:
                files = {
                    'file': (file_name, file)
                }
                result = self.execute_request(
                    method=RequestMethods.POST,
                    url=url,
                    headers=headers,
                    files=files,
                    data=data
                )
                return result
        else:
            logger.info(f'Provided file path: "{document_path}" is not valid')
        return None

    # Completions
    def perform_completions(
            self,
            input_str: str,
            collection_ids: str | list[str],
            flow: FlowTypes = FlowTypes.SEARCH,
            search_limit: int = 5,
            completion_model_id: str = None,
            embedding_model_id: str = None,
            document_ids: list[str] | None = None
    ) -> CompletionsResponse:
        logger.debug(f'Performing completions ... ')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.completions.base)
        payload = {
            "question": input_str,
            "flow": flow.value if isinstance(flow, FlowTypes) else None,
            "collectionIds": collection_ids if isinstance(collection_ids, list) else [collection_ids],
            "completionModelId": completion_model_id,
            "limit": search_limit,
            "documentIds": document_ids
        }
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        result = self.execute_request(
            method=RequestMethods.POST,
            url=url,
            headers=headers,
            data=json.dumps(payload),
            timeout=20.0
        )
        if result:
            return CompletionsResponse(**result)
        else:
            return CompletionsResponse().init_with_none()

    # Models
    def get_ai_models(self) -> list[AIModels]:
        logger.debug(f'Getting all AI models ... ')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.model_specification.base)
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=self.get_headers()
        )
        models = []
        for model in result:
            models.append(AIModels(**model))
        return models

    def get_ai_model_by_id(self, model_id: str) -> AIModels:
        logger.debug(f'Getting AI model by id: {model_id} ... ')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.model_specification.by_id)
        url = url.format(id=model_id)
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=self.get_headers()
        )
        return AIModels(**result)

    def get_ai_models_by_operation(self,
                                   operation: ModelOperation = ModelOperation.EMBEDDING
                                   ) -> list[AIModels]:
        logger.debug(f'Getting AI models by operation: {operation} ... ')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.model_specification.operation)
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=self.get_headers(),
            params={
                "operation": operation.value
            }
        )
        models = []
        for model in result:
            models.append(AIModels(**model))
        return models

    # Documents
    def upload_documents(self, document_path: str, file_name: str, tag_ids: list):
        logger.debug(f'Uploading file: {file_name} ... ')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document.upload)
        headers = self.get_headers()
        data = {
            "fileName": file_name,
            "tagIds": tag_ids
        }
        files = {}
        result = None
        if os.path.isfile(document_path):
            with open(document_path, 'rb') as file:
                files = {
                    'file': (file_name, file)
                }
                result = self.execute_request(
                    method=RequestMethods.POST,
                    url=url,
                    headers=headers,
                    files=files,
                    data=data
                )
        else:
            logger.info(f'Provided file path: "{document_path}" is not valid')

        return Documents(**result)

    def get_document_collection(self) -> list[Documents]:
        logger.debug(f'Getting default document collections')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document.search)
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=self.get_headers()
        )
        documents = []
        if 'content' in result:
            for collection_details in result['content']:
                documents.append(Documents(**collection_details))
        return documents

    def rename_document(self, document_id: str, new_name: str) -> str:
        logger.debug(f'Rename document by ID')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document.by_id)
        url = url.format(id=document_id)
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        result = self.execute_request(
            method=RequestMethods.PATCH,
            url=url,
            headers=headers,
            data=json.dumps({'name': new_name})
        )
        return result

    def get_document_by_id(self, document_id: str) -> Documents:
        logger.debug(f'Getting document by ID')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document.by_id)
        url = url.format(id=document_id)
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=self.get_headers()
        )
        if result:
            return Documents(**result)
        else:
            None

    def delete_document_by_id(self, document_id: str):
        logger.debug(f'Delete document by ID')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document.by_id)
        url = url.format(id=document_id)
        result = self.execute_request(
            method=RequestMethods.DELETE,
            url=url,
            headers=self.get_headers()
        )
        return result

    # permission

    # Notes
    def search_notes(self, filter_params: dict = None):
        pass

    def get_note_by_id(self, note_id: str):
        pass

    def create_note(self):
        pass

    def update_note(self):
        pass

# -------------------------------------------------------------------------------------------------------------------- #
