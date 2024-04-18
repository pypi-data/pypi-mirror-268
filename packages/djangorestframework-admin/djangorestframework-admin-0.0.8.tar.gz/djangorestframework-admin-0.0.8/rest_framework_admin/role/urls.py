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

from rest_framework_admin.role import views
from rest_framework_admin.role.permission.urls import urlpatterns as permission_urlpatterns
from rest_framework_util.routers import RelDefaultRouter

role_router = routers.DefaultRouter()
role_router.register(r'^roles', views.RoleModelViewSet)

role_permission_rel_router = RelDefaultRouter()
role_permission_rel_router.register(
    r'^permissions',
    views.RolePermissionRelModelViewSet,
    basename='role_permission_rel_router')

role_member_rel_router = RelDefaultRouter()
role_member_rel_router.register(
    r'^members',
    views.RoleMemberRelModelViewSet,
    basename='role_member_rel_router')


urlpatterns = [
    path(r'', include(role_router.urls)),
    re_path(
        r'roles/(?P<role_id>[a-z0-9A-Z\-]{32})/',
        include(
            role_permission_rel_router.urls)),
    re_path(
        r'roles/(?P<role_id>[a-z0-9A-Z\-]{32})/',
        include(
            role_member_rel_router.urls)),
    re_path(r'^members/$', views.MemberListAPIView.as_view()),
] + permission_urlpatterns
