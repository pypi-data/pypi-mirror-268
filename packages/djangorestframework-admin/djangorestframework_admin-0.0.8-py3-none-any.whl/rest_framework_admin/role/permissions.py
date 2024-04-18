#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/12/22
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from rest_framework import permissions


class RoleModelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin_or_owner

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin_or_owner


class RolePermissionRelModelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin_or_owner

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin_or_owner


class RoleMemberRelModelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin_or_owner

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin_or_owner


class MemberListPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin_or_owner
