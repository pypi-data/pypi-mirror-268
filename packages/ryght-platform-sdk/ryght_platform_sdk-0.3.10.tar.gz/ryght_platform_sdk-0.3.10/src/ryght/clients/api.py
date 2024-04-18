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

# from ryght.interface import NotesAPI
from ryght.interface import ModelsAPI
from ryght.interface import DocumentsAPI
from ryght.interface import CompletionsAPI
from ryght.interface import ConversationsAPI
from ryght.interface import DocumentCollectionAPI
# from ryght.interface import PermissionManagementAPI


# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Logger Definition |--->
# -------------------------------------------------------------------------------------------------------------------- #
logger = logging.getLogger(__name__)


# -------------------------------------------------------------------------------------------------------------------- #
# <---| * Class Definition |--->
# -------------------------------------------------------------------------------------------------------------------- #
class ApiClient(
    ModelsAPI,
    DocumentsAPI,
    CompletionsAPI,
    ConversationsAPI,
    DocumentCollectionAPI
):
    pass

# -------------------------------------------------------------------------------------------------------------------- #
