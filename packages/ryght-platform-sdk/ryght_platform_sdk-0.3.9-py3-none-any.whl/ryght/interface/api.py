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
import time
import json
import logging
from json import JSONDecodeError
from urllib.parse import urljoin
from urllib.parse import urlencode
from pydantic import ValidationError

from ryght.models import Token
from ryght.utils import QnARating
from ryght.configs import Credentials
from ryght.configs import ApiEndpoints
from ryght.utils import RequestMethods
from ryght.managers import TokenManager
from ryght.requests import HttpxRequestExecutor
from result import Result, is_ok, is_err, OkErr, Ok, Err, as_result

from ryght.models import (
    Prompts,
    Collection,
    AIModels,
    Documents,
    TraceStatus,
    JsonDocument,
    ConversationInfo,
    CompletionsResponse,
    ConversationResponse,
    ChunkedDocumentCollection,
)

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
            if method == RequestMethods.GET:
                request_fn = self.http_request_exec.get
            elif method == RequestMethods.PUT:
                request_fn = self.http_request_exec.put
            elif method == RequestMethods.POST:
                request_fn = self.http_request_exec.post
            elif method == RequestMethods.PATCH:
                request_fn = self.http_request_exec.patch
            elif method == RequestMethods.DELETE:
                request_fn = self.http_request_exec.delete
            else:
                raise ValueError(f'Unknown method {method}')

            response = request_fn(url=url, **kwargs)

            if response.status_code == 200:
                if response.headers.get('Content-Type') == 'application/json':
                    return response.json()
                else:
                    return f'Success! response code: {response.status_code}'
            elif response.status_code == 201:
                if response.headers.get('Content-Type') == 'application/json':
                    return response.json()
                else:
                    return f'Success! response code: {response.status_code}'
            elif response.status_code == 202:
                if response.headers.get('Content-Type') == 'application/json':
                    return response.json()
                elif response.text is not None and response.text != '':
                    value = response.text
                else:
                    return f'Success! response code: {response.status_code}'
            elif response.status_code in [203, 204]:
                if response.text is not None and response.text != '':
                    value = response.text
                else:
                    value = f'Success! response code: {response.status_code}'
                return value
            elif response.status_code in [401, 403, 404]:
                logger.error(
                    f'Got client error: {response.status_code}, Please check your credential & api endpoint variables'
                )
                response.raise_for_status()
            elif response.status_code in [500]:
                logger.error('Got client error: 500, attempting new token request after 5 seconds')
                time.sleep(5)
                response = request_fn(url=url, **kwargs)
                response.raise_for_status()
            else:
                logger.error(f'Unknown response status code: {response.status_code}')

        except ValueError as value_error:
            logger.error(f'ValueError occurred: {value_error}')
        except Exception as exception:
            logger.error('Exception occurred: {}'.format(exception))


# -------------------------------------------------------------------------------------------------------------------- #
class Conversations(ApiInterface):

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
        logger.debug(f'Loading all question and anwsers for conversation ...')
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

