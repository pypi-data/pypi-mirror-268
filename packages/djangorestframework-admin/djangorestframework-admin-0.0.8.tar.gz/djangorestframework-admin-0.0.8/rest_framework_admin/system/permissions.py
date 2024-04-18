#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/10/19
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['ConfigPermission']

from rest_framework import permissions


class ConfigPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ('selection',):
            return True
        return request.user.is_admin_or_owner()

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin_or_owner()
