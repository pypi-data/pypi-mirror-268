#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/10/10
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['urlpatterns']

from django.urls import path, re_path, include

from rest_framework_admin.system import views
from rest_framework_util.decorators import login_exempt_func


def __login_exempt(request, view):
    return request.method.upper() == 'GET'


_urlpatterns = ([
    re_path(
        r'^configs/$',
        login_exempt_func(
            views.SysConfigAPIView.as_view(), func=__login_exempt)),
    re_path(r'^files/upload/$', views.FileUploadAPIView.as_view()),
    re_path(r'^files/merge/$', views.FileMergeAPIView.as_view()),
], 'scm',)


urlpatterns = [
    path('', include(_urlpatterns)),
]
