#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2024/1/2
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['urlpatterns']

from django.urls import re_path, include, path

from rest_framework_admin.auth import views
from rest_framework_util.decorators import login_exempt

from rest_framework_admin.auth.jwt.urls import urlpatterns as jwt_urlpatterns

urlpatterns = [
    re_path(r'me/$', views.AuthMeRetrieveAPIView.as_view()),
    re_path(
        r'register/$',
        login_exempt(
            views.AuthRegisterCreateAPIView.as_view())),
    path('jwt/', include(jwt_urlpatterns))
]
