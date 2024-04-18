#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/12/8
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from rest_framework import permissions

from rest_framework_admin.user.configs import MemberRoleEnum


class GroupModelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        if view.action in ('create', ):
            return request.user.is_admin_or_owner
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin_or_owner:
            return True
        user_rel = obj.user_rel.filter(user_id=request.user.id).first()
        if not user_rel:
            return False
        if view.action in ('retrieve',):
            return True
        return MemberRoleEnum.is_admin_or_owner(user_rel.role)


class GroupUserRelModelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        if request.user.is_admin_or_owner:
            return True
        user_rel = view.get_queryset().filter(user_id=self.request.user.id)
        if not user_rel:
            return False
        if view.action in ('retrieve', ):
            return True
        return MemberRoleEnum.is_admin_or_owner(user_rel.role)

    def has_object_permission(self, request, view, obj):
        return False
