#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2024/4/15
__all__ = ['api_settings']

from rest_framework_util.settings import get_api_settings

DEFAULTS = {
    'UPLOAD_SETTINGS': 'rest_framework_util.core.upload.settings.UploadSettings',
    # 用户可用用于的最大空间数
    'MAX_TENANT_PER_USER': 3,
}

IMPORT_STRINGS = [
    'UPLOAD_SETTINGS'
]

api_settings = get_api_settings(
    'ADMIN_TENANT',
    defaults=DEFAULTS,
    import_strings=IMPORT_STRINGS)
