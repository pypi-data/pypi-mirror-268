#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/12/24 13:04
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['api_settings']

from rest_framework_util.settings import get_api_settings

DEFAULTS = {
    'UPLOAD_SETTINGS': 'rest_framework_util.core.upload.settings.UploadSettings'
}

IMPORT_STRINGS = [
    'UPLOAD_SETTINGS'
]

api_settings = get_api_settings(
    'ADMIN_SYSTEM',
    defaults=DEFAULTS,
    import_strings=IMPORT_STRINGS)
