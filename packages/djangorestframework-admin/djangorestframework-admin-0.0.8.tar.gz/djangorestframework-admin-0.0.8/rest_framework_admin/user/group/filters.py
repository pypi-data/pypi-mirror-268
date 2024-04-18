#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from django_filters import rest_framework as filters
from rest_framework_admin.group.filters import BaseGroupFilter
from rest_framework_admin.user.group.models import Group, GroupUserRel


class GroupFilter(BaseGroupFilter):

    class Meta(BaseGroupFilter.Meta):
        model = Group


class GroupUserRelFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='user__name', lookup_expr='icontains')

    class Meta:
        model = GroupUserRel
        fields = ['name']
