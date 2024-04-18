#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from django_filters import rest_framework as filters

from rest_framework_admin.user.models import User, GroupUserRel


class UserFilter(filters.FilterSet):
    is_active = filters.BooleanFilter()

    class Meta:
        model = User
        fields = ['is_active']


class GroupUserRelFilter(filters.FilterSet):
    id = filters.CharFilter(field_name='group_id')

    name = filters.CharFilter(
        lookup_expr='icontains',
        field_name='group__name')

    class Meta:
        model = GroupUserRel
        fields = ['id', 'name']
