#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from django_filters import rest_framework as filters

from rest_framework_admin.tenant.models import Tenant, TenantUserRel


class TenantFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tenant
        fields = ['name']


class TenantUserRelFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='user_id')

    name = filters.CharFilter(
        lookup_expr='icontains',
        field_name='user__username')

    class Meta:
        model = TenantUserRel
        fields = ['id', 'name']
