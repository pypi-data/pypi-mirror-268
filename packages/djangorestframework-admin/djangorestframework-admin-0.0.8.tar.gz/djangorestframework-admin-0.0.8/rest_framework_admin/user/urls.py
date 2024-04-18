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

from rest_framework_admin.user import views
from rest_framework_admin.user.group.urls import urlpatterns as group_urlpatterns
from rest_framework_admin.user.me.urls import urlpatterns as me_urlpatterns
from rest_framework_util.routers import RelDefaultRouter

user_router = routers.DefaultRouter()
user_router.register(r'^users', views.UserModelViewSet)

group_user_rel_router = RelDefaultRouter()
group_user_rel_router.register(
    r'^groups',
    views.GroupUserRelModelViewSet,
    basename='group_user_rel_router')

urlpatterns = [
    path(r'', include(user_router.urls)),
    re_path(
        r'users/(?P<user_id>[a-z0-9A-Z\-]{32})/',
        include(
            group_user_rel_router.urls)),
] + group_urlpatterns + me_urlpatterns
