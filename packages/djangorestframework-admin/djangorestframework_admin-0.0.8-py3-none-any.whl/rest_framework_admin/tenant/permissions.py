#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/12/8
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from rest_framework import permissions

from rest_framework_admin.tenant.models import Tenant, TenantUserRel
from rest_framework_admin.tenant.settings import api_settings
from rest_framework_admin.user.configs import MemberRoleEnum


class TenantModelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if view.action == 'create':
            return TenantUserRel.objects.filter(
                user_id=request.user.id,
                role=MemberRoleEnum.owner.name).count() < api_settings.MAX_TENANT_PER_USER
        elif view.action == 'select':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_admin_or_owner:
            return True
        rel = obj.user_rels.filter(user_id=request.user.id)
        if not rel.exists():
            return False
        if view.action in ('retrieve', ):
            return True
        return MemberRoleEnum.is_admin_or_owner(rel.role)


class TenantUserRelModelPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_admin_or_owner:
            return True
        if request.user.is_staff:
            return True
        tenant = view.get_parent_object()
        rel = tenant.user_rels.filter(user_id=request.user.id)
        if not rel.exists():
            return False
        if view.action in ('list',):
            return True
        return MemberRoleEnum.is_admin_or_owner(rel.role)

    def has_object_permission(self, request, view, obj):
        return False
