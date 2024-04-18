#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from django_filters import rest_framework as filters

from rest_framework_admin.role.configs import MemberTypeEnum
from rest_framework_admin.role.models import Role, RolePermissionRel, RoleMemberRel, Permission


class RoleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    code = filters.CharFilter(lookup_expr='icontains')
    type = filters.CharFilter(method='filter_by_type')

    class Meta:
        model = Role
        fields = ['name', 'code', 'type']

    def filter_by_type(self, queryset, name, value):
        return queryset.filter(type__in=value.split(','))


class RolePermissionRelFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='permission_id')
    name = filters.CharFilter(
        lookup_expr='icontains',
        field_name='permission__name')

    class Meta:
        model = RolePermissionRel
        fields = ['id', 'name']


class RoleMemberRelFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='member_id')
    type = filters.CharFilter(field_name='member_type')

    class Meta:
        model = RoleMemberRel
        fields = ['id', 'type']
