#!/usr/bin/python
# -*- coding:utf-8 -*-
# DateTime:2023/6/21
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['AuthBackend']


from django.utils.translation import gettext_lazy as _
from django.contrib.auth.backends import ModelBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

from rest_framework_admin.auth import logger
from rest_framework_admin.auth.jwt.utils import blacklist


class AuthBackend(ModelBackend):
    def authenticate(self, request, is_jwt_token=False, **kwargs):
        if not is_jwt_token:
            return None
        try:
            user_auth_tuple = JWTAuthentication().authenticate(request)
        except InvalidToken:
            logger.exception(_('JWT无效'))
            user_auth_tuple = None
        except BaseException:
            logger.exception(_('JWT认证失败'))
            user_auth_tuple = None
        if user_auth_tuple is None:
            return None
        user, token = user_auth_tuple
        if blacklist.has_token(token):
            return None
        return user
