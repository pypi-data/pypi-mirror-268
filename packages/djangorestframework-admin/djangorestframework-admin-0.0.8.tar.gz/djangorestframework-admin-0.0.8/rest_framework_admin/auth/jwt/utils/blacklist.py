#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/10/11
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['has_token', 'add_by_user']

import time

from django.utils.translation import gettext_lazy as _
from django.core.cache import cache
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from rest_framework_admin.auth import logger


def has_token(token: RefreshToken | AccessToken) -> bool:
    """ token是否在黑名单

    :param token: access或refresh token
    :return: True/False
    """
    jti = token.payload['jti']
    return cache.get(jti, None)


def add_by_user(user):
    user_id = user
    cache_data = cache.get(user_id, None)
    if not (cache_data and isinstance(cache_data, dict)):
        logger.info(_(f'没有找到缓存数据, key={user_id}'))
        return
    ts = int(time.time())
    try:
        for key, jti in cache_data.items():
            cache.set(jti, f'{user_id}_{ts}')
    except BaseException:
        logger.exception(_(f'增加jwt黑名单异常. data={cache_data}'))
    cache.delete(user_id)
