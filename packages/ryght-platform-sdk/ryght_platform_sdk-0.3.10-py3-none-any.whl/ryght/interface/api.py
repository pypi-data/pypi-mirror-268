# <---| * Module Information |--->
# ==================================================================================================================== #
"""
    :param FileName     :   api.py
    :param Author       :   Sudo
    :param Date         :   2/07/2024
    :param Copyright    :   Copyright (c) 2024 Ryght, Inc. All Rights Reserved.
    :param License      :   #
    :param Description  :   #
"""
__author__ = 'Data engineering team'
__copyright__ = 'Copyright (c) 2024 Ryght, Inc. All Rights Reserved.'

# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Import section |--->
# -------------------------------------------------------------------------------------------------------------------- #
import os
import time
import json
import logging
from urllib.parse import urljoin
from urllib.parse import urlencode
from pydantic import ValidationError

from ryght.models import Token
from ryght.utils import QnARating
from ryght.configs import Credentials
from ryght.configs import ApiEndpoints
from ryght.managers import TokenManager
from ryght.requests import HttpxRequestExecutor
from ryght.utils import RequestMethods, FlowTypes, ModelOperation
from result import Result, is_ok, is_err, OkErr, Ok, Err, as_result

from ryght.models import Prompts
from ryght.models import AIModels
from ryght.models import Documents
from ryght.models import Collection
from ryght.models import TraceStatus
from ryght.models import JsonDocument
from ryght.models import ConversationInfo
from ryght.models import CompletionsResponse
from ryght.models import ConversationResponse
from ryght.models import ChunkedDocumentCollection

# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Logger Definition |--->
# -------------------------------------------------------------------------------------------------------------------- #
logger = logging.getLogger(__name__)


# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Class Definition |--->
# -------------------------------------------------------------------------------------------------------------------- #
class ApiInterface:
    api_endpoints: ApiEndpoints
    token_manager: TokenManager
    http_request_exec: HttpxRequestExecutor

    def __init__(self, env: str = 'production'):
        self.api_endpoints = ApiEndpoints.load_api_endpoints(env=env)
        self.http_request_exec = HttpxRequestExecutor()
        self.token_manager: TokenManager = TokenManager(
            token=Token.init_as_none(),
            credentials=Credentials.init_none(),
            requestor=self.http_request_exec,
            auth_url=self.api_endpoints.auth_token_url
        )

    def get_headers(self):
        return {'Authorization': self.token_manager.token.authorization_param}

    @TokenManager.authenticate
    def execute_request(
            self,
            method: RequestMethods,
            url,
            **kwargs
    ) -> dict | str:

        try:
            match method:
                case RequestMethods.GET:
                    request_fn = self.http_request_exec.get
                case RequestMethods.PUT:
                    request_fn = self.http_request_exec.put
                case RequestMethods.POST:
                    request_fn = self.http_request_exec.post
                case RequestMethods.PATCH:
                    request_fn = self.http_request_exec.patch
                case RequestMethods.DELETE:
                    request_fn = self.http_request_exec.delete
                case _:
                    raise ValueError(f'Unknown method {method}')

            response = request_fn(url=url, **kwargs)

            match response.status_code:
                case 200 | 201 | 202 | 203 | 204:
                    if response.headers.get('Content-Type') == 'application/json':
                        return response.json()
                    elif response.text is not None and response.text != '':
                        value = response.text
                        return f'Success! response text: {value}'
                    else:
                        return f'Success! response code: {response.status_code}'

                case 400 | 402 | 403 | 404:
                    logger.error(
                        f'Got client error: {response.status_code}, '
                        f'Please check your credential & api endpoint variables'
                    )
                    response.raise_for_status()

                case 500 | 502 | 503 | 504:
                    logger.error('Got client error: 500, attempting new token request after 5 seconds')
                    time.sleep(5)
                    # try this outside this func
                    response = request_fn(url=url, **kwargs)
                    response.raise_for_status()

                case _:
                    logger.error(f'Unknown response status code: {response.status_code}')
        except ValueError as value_error:
            logger.error(f'ValueError occurred: {value_error}')
        except Exception as exception:
            logger.error('Exception occurred: {}'.format(exception))


# -------------------------------------------------------------------------------------------------------------------- #
class DocumentCollectionAPI(ApiInterface):
    @as_result(NotImplementedError)
    def get_collection_page_by_page(self, query_params: dict = None):
        raise NotImplementedError(f'Get collections page by page not implemented !')

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


# -------------------------------------------------------------------------------------------------------------------- #
class CompletionsAPI(ApiInterface):
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


# -------------------------------------------------------------------------------------------------------------------- #
class ModelsAPI(ApiInterface):
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


# -------------------------------------------------------------------------------------------------------------------- #
class DocumentsAPI(ApiInterface):
    # Documents
    def upload_documents(self, document_path: str, file_name: str, tag_ids: list):
        logger.debug(f'Uploading file: {file_name} ... ')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.document.upload)
        headers = self.get_headers()
        data = {
            "fileName": file_name,
            "tagIds": tag_ids
        }
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
            return None

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


# -------------------------------------------------------------------------------------------------------------------- #
class ConversationsAPI(ApiInterface):
    @as_result(Exception, ValueError, ValidationError, TypeError)
    def find_user_conversations(self, query_params: dict = None) -> list[ConversationInfo]:
        logger.debug(f'Conversations of the current user ...')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.conversations.base)
        if isinstance(query_params, dict):
            url = urljoin(url, '?' + urlencode(query_params))
            print(url)
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=self.get_headers()
        )
        conversations_list = []
        if 'content' in result:
            for collection_details in result['content']:
                conversations_list.append(ConversationInfo(**collection_details))
            return conversations_list
        else:
            raise Exception('Content is not found in the response, Parsing Error.')

    @as_result(Exception, ValueError, ValidationError, TypeError)
    def update_conversation_name(
            self,
            conversation_id: str,
            new_name: str
    ) -> str:
        logger.debug(f'update a given conversation by its ID')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.conversations.base)
        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'

        payload = {
            'id': conversation_id,
            'name': new_name
        }

        result = self.execute_request(
            method=RequestMethods.PUT,
            url=url,
            headers=headers,
            data=json.dumps(payload)
        )
        if result is None:
            raise Exception(f'Got None as response, response: {result}')
        else:
            return result

    @as_result(Exception, ValueError, ValidationError, TypeError)
    def converse(
            self,
            question: str,
            conversation_id: str,
            collection_ids: str | list[str] | None = None,
            default_collection: bool = False,
            document_ids: list[str] | None = None,
            copilot_id: str | None = None,
            prompt: Prompts | None = None
    ) -> ConversationResponse:
        logger.debug(f'update a given conversation by its ID')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.conversations.base)

        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'

        payload = {
            "question": question,
            "conversationId": conversation_id,
            "collectionIds": collection_ids if isinstance(collection_ids, list) else [collection_ids],
            "defaultCollection": default_collection,
            "documentIds": document_ids,
            "copilotId": copilot_id,
            "prompt": prompt.model_dump_json() if prompt else prompt
        }

        result = self.execute_request(
            method=RequestMethods.POST,
            url=url,
            headers=headers,
            data=json.dumps(payload),
            timeout=15.0
        )
        if result is None:
            raise Exception(f'Got None as response, response: {result}')
        else:
            return ConversationResponse(**result)

    @as_result(Exception, ValueError, ValidationError, TypeError)
    def send_feedback(
            self,
            feedback_message: str,
            question_answer_id: str,
            rating: QnARating
    ) -> str:
        logger.debug(f'Feedback for QnA ...')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.conversations.feedback)

        headers = self.get_headers()
        headers['Content-Type'] = 'application/json'
        payload = {
            "content": feedback_message,
            "questionAnswerId": question_answer_id,
            "rate": rating.value if isinstance(rating, QnARating) else None
        }

        result = self.execute_request(
            method=RequestMethods.POST,
            url=url,
            headers=headers,
            data=json.dumps(payload)
        )
        if result is None:
            raise Exception(f'Got None as response, response: {result}')
        else:
            return result

    @as_result(Exception, ValueError, ValidationError, TypeError)
    def delete_conversation_by_id(self, conversation_id: str):
        logger.debug(f'Deleting a conversation by its ID ...')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.conversations.by_id)
        url = url.format(id=conversation_id)
        result = self.execute_request(
            method=RequestMethods.PATCH,
            url=url,
            headers=self.get_headers()
        )
        if result is None:
            raise Exception(f'Got None as response, response: {result}')
        else:
            return result

    @as_result(Exception, ValueError, ValidationError, TypeError)
    def get_all_question_and_answers(self, conversation_id: str) -> list[ConversationResponse]:
        logger.debug(f'Loading all question and answers for conversation ...')
        url = urljoin(self.api_endpoints.base_url, self.api_endpoints.conversations.by_id)
        url = url.format(id=conversation_id)
        result = self.execute_request(
            method=RequestMethods.GET,
            url=url,
            headers=self.get_headers()
        )
        question_and_answers = []
        if 'content' in result:
            for collection_details in result['content']:
                question_and_answers.append(ConversationResponse(**collection_details))
            return question_and_answers
        else:
            raise Exception('Content is not found in the response, Parsing Error.')


# -------------------------------------------------------------------------------------------------------------------- #
class NotesAPI(ApiInterface):
    pass


# -------------------------------------------------------------------------------------------------------------------- #
class PermissionManagementAPI(ApiInterface):
    pass

# -------------------------------------------------------------------------------------------------------------------- #
