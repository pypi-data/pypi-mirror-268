#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/12/22
# Tool:PyCharm

"""  """
__version__ = '0.0.8'
__history__ = """"""
__all__ = ['INSTALLED_APPS', 'logger']

import logging

logger = logging.getLogger('django.rest_framework_admin')

INSTALLED_APPS = [
    'django_filters',
    'drf_spectacular',
    'rest_framework_simplejwt'
]
