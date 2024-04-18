#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['urlpatterns']

from django.urls import path, include, re_path
from rest_framework import routers

from rest_framework_admin.user.me import views


me_router = routers.DefaultRouter()
me_router.register(r'^me', views.MeModelViewSet)

urlpatterns = [
    path('', include(me_router.urls)),
    re_path(r'^me/$', views.UpdateUserModelApiView.as_view()),
]
