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
import logging

from ryght.interface import BaseClient
from ryght.configs import Credentials, ApiEndpoints
from ryght.models import Documents, Collection, AIModels, JsonDocument, ChunkedDocumentCollection

# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Logger Definition |--->
# -------------------------------------------------------------------------------------------------------------------- #
logger = logging.getLogger(__name__)


# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Class Definition |--->
# -------------------------------------------------------------------------------------------------------------------- #
class RyghtClient(BaseClient):
    """
        A client for user to access the Ryght features using the Ryght backend APIs

        You can access the following features using this class,
            - Get a list of all document collections
            - Create a new empty document collection
            - Get a document collection by its ID
            - Perform Completions
            - Get a list of all AI models
            - Get a list of AI models by its operation nature
            - Get an AI model by its ID
            - Get a list of all the documents from default collections
            - Upload a new document to the default collection
            - Get a document from default collections by its ID
            - Delete a document from default collections by its ID
            - Rename a document in default collections by its ID
    """
    pass


# -------------------------------------------------------------------------------------------------------------------- #

class DevClient(BaseClient):
    """
        A client for user to access the Ryght features using the Ryght backend APIs, but with some specialized functions
    for developers and development purposes.

        You can access all the features of RyghtClient and get the following features in addition,
            - Upload a new document to the document collection
            - Upload a new pdf document to the document collection
            - Get status using trace ID
            - Create/Upload a pre-chunked documentCollection
    """
    def __repr__(self):
        return f"Client is Configured to the Environment: {self.environment} for the Organization: {self.organization}"

    def get_client_config(self):
        return {
            "environment": self.environment,
            "organization": self.organization
        }

    def switch_environment(self, env: str, credentials: dict | Credentials | str):
        try:
            self.api_client.api_endpoints = ApiEndpoints.load_api_endpoints(env=env)
            self.api_client.token_manager.auth_url = self.api_client.api_endpoints.auth_token_url
            self.set_credentials(credentials)
            self.api_client.token_manager.get_new_token(organization=self.organization)
        except Exception as e:
            logger.error(e)
        else:
            self.api_client.environment = env
            self.environment = env

    def switch_organization(self, org: str):
        try:
            self.api_client.token_manager.get_new_token(organization=org)
            self.api_client.token_manager.credentials.organization = org
        except Exception as e:
            logger.error(e)
        else:
            self.organization = org

    def create_a_chunked_collection(
            self,
            chunked_document_collection: ChunkedDocumentCollection
    ) -> str:
        return self.api_client.upload_chunked_document_collection(chunked_document_collection)

# -------------------------------------------------------------------------------------------------------------------- #
