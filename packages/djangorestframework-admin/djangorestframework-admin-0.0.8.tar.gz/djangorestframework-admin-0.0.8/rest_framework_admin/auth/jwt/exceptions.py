#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['AuthVerifyError']

from django.utils.translation import gettext_lazy as _
from rest_framework_util.exceptions import HTTP400


class AuthVerifyError(HTTP400):
    MESSAGE = _("JWT认证错误")
    ERROR_CODE = "40101"
