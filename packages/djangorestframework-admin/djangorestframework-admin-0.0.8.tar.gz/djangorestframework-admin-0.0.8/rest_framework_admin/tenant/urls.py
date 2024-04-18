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

from rest_framework_admin.tenant import views
from rest_framework_util.routers import RelDefaultRouter

tenant_router = routers.DefaultRouter()
tenant_router.register(r'^tenants', views.TenantModelViewSet)

tenant_user_rel_router = RelDefaultRouter()
tenant_user_rel_router.register(
    r'^users',
    views.TenantUserRelModelViewSet,
    basename='tenant_user_rel_router')


urlpatterns = [
    path(r'', include(tenant_router.urls)),
    re_path(
        r'tenants/(?P<tenant_id>[a-z0-9A-Z\-]{32})/',
        include(
            tenant_user_rel_router.urls)),
]
