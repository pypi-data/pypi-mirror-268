#!/usr/bin/python
# -*- coding:utf-8 -*-
# DateTime:2023/6/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['urlpatterns']

from django.urls import path

from rest_framework_util.decorators import login_exempt
from rest_framework_admin.auth.jwt import views

urlpatterns = [
    path(
        'login/',
        login_exempt(views.LoginAPIView.as_view()),
        name='jwt_login'),
    path(
        'logout/',
        login_exempt(views.LogoutAPIView.as_view()),
        name='jwt_logout'),
    path(
        'refresh/',
        login_exempt(views.RefreshAPIView.as_view()),
        name='jwt_refresh'),
]
