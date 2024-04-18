#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from django_filters import rest_framework as filters

from rest_framework_admin.role.permission.models import Permission


class PermissionFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    content_type = filters.CharFilter()
    action = filters.CharFilter()

    class Meta:
        model = Permission
        fields = ['name', 'content_type', 'action']
