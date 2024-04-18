#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Value, CharField, Q
from django.utils import timezone

from rest_framework_admin.role.configs import MemberTypeEnum
from rest_framework_admin.user.group.models import Group
from rest_framework_util.db.models.base import BaseModel, BaseRelModel
from rest_framework_admin.role.permission.models import Permission


class BaseRole(BaseModel):
    code = models.CharField('编码', max_length=64)
    type = models.CharField('类型', max_length=32)
    weight = models.PositiveSmallIntegerField(
        '权重，值越高优先级越高，即权限越大')
    # permissions = models.ManyToManyField(
    #     Permission, through='RolePermissionRel', through_fields=(
    #         'role', 'permission'), related_name='roles')

    class Meta:
        abstract = True

    @staticmethod
    def filter_by_member(member_id, member_type, is_valid=None):
        """ 过滤直接绑定的角色 """
        queryset = Role.objects.filter(
            member_rels__member_id=member_id,
            member_rels__member_type=member_type)
        queryset = queryset.annotate(
            member_id=Value(
                member_id,
                output_field=CharField(
                    max_length=32)),
            member_type=Value(member_type, output_field=CharField(max_length=32)))
        if is_valid is None:
            return queryset
        if is_valid:
            queryset = queryset.filter(Q(member_rels__expire_datetime__isnull=True) | Q(
                member_rels__expire_datetime__lt=timezone.now()))
        else:
            queryset = queryset.exclude(
                member_rels__expire_datetime__isnull=True).filter(
                member_rels__expire_datetime__gte=timezone.now())
        return queryset

    @staticmethod
    def filter_by_valid(queryset, is_valid, **kwargs):
        if is_valid is None:
            return queryset
        if is_valid:
            queryset = queryset.filter(Q(expire_datetime__isnull=True) | Q(
                expire_datetime__lt=timezone.now()))
        else:
            queryset = queryset.exclude(
                expire_datetime__isnull=True).filter(
                expire_datetime__gte=timezone.now())
        return queryset.filter(**kwargs)

    def extended_strs(self):
        return [f'code={self.code}',
                f'type={self.type}',
                f'weight={self.weight}']


class Role(BaseRole):
    permissions = models.ManyToManyField(
        Permission, through='RolePermissionRel', through_fields=(
            'role', 'permission'), related_name='roles')

    class Meta:
        db_table = 'role'
        verbose_name = '角色表'

    def filter_users(self, is_valid=None, **kwargs):
        queryset = self.member_rels.filter(
            member_type=MemberTypeEnum.user.name)
        queryset = self.filter_by_valid(queryset, is_valid)
        # TODO(fengdy): 调整为子查询
        return get_user_model().objects.filter(
            id__in=queryset.values_list('member_id', flat=True))

    def filter_groups(self, is_valid=None, **kwargs):
        queryset = self.member_rels.filter(
            member_type=MemberTypeEnum.group.name)
        queryset = self.filter_by_valid(queryset, is_valid)
        return Group.objects.filter(
            id__in=queryset.values_list('member_id', flat=True))

    def save_users(self, user_ids, **kwargs):
        return RoleMemberRel.save_by_role(
            self.id, user_ids, MemberTypeEnum.user.name, **kwargs)

    def save_groups(self, group_ids, **kwargs):
        return RoleMemberRel.save_by_role(
            self.id, group_ids, MemberTypeEnum.group.name, **kwargs)

    def delete_users(self, user_ids=None):
        return RoleMemberRel.delete_by_role(
            self.id, user_ids, MemberTypeEnum.user.name)

    def delete_groups(self, group_ids=None):
        return RoleMemberRel.delete_by_role(
            self.id, group_ids, MemberTypeEnum.group.name)


class BaseRolePermissionRel(BaseRelModel):

    class Meta:
        abstract = True


class RolePermissionRel(BaseRolePermissionRel):
    role = models.ForeignKey(Role, models.CASCADE, related_name='permission_rels')
    permission = models.ForeignKey(Permission, models.CASCADE, related_name='role_rels')

    class Meta:
        db_table = 'role_permission_rel'
        verbose_name = '角色权限关联表'
        unique_together = ('role', 'permission')

    def extended_strs(self):
        return [f'role={self.role.id}',
                f'permission={self.permission.id}']


class BaseRoleMemberRel(BaseRelModel):
    member_id = models.CharField(help_text='主体id，用户id/组id', max_length=32)
    # role = models.ForeignKey(
    #     Role,
    #     models.RESTRICT,
    #     related_name='member_rels')
    member_type = models.CharField(help_text='主体类型，用户/组', max_length=32)
    expire_datetime = models.DateTimeField('过期时间', blank=True, null=True)

    class Meta:
        abstract = True

    def extended_strs(self):
        return [f'role={self.role.id}',
                f'member_id={self.member_id}',
                f'member_type={self.member_type}']

    @property
    def member(self):
        if self.member_type == MemberTypeEnum.group.name:
            return Group.objects.get(pk=self.member_id)
        else:
            return get_user_model().objects.get(pk=self.member_id)

    @classmethod
    def save_by_role(cls, role_id, member_ids, member_type, **kwargs):
        if not isinstance(member_ids, (tuple, list)):
            member_ids = [member_ids]
        for member_id in member_ids:
            kwargs['role_id'] = role_id
            kwargs['member_id'] = member_id
            kwargs['member_type'] = member_type
            rel = cls(**kwargs)
            rel.save()

    @classmethod
    def save_by_member(cls, member_id, role_ids, member_type, **kwargs):
        if not isinstance(role_ids, (tuple, list)):
            role_ids = [role_ids]
        for role_id in role_ids:
            kwargs['role_id'] = role_id
            kwargs['member_id'] = member_id
            kwargs['member_type'] = member_type
            rel = cls(**kwargs)
            rel.save()

    @classmethod
    def delete_by_role(cls, role_id, member_ids, member_type):
        kwargs = {
            'member_type': member_type,
            'role_id': role_id
        }
        if member_ids is None:
            cls.objects.filter(**kwargs).delete()
            return
        if not isinstance(member_ids, (tuple, list)):
            member_ids = [member_ids]
            kwargs['member_id__in'] = member_ids
        cls.objects.filter(**kwargs).delete()

    @classmethod
    def delete_by_member(cls, member_id, role_ids, member_type):
        kwargs = {
            'member_type': member_type,
            'member_id': member_id
        }
        if role_ids is None:
            cls.objects.filter(**kwargs).delete()
            return
        if not isinstance(role_ids, (tuple, list)):
            role_ids = [role_ids]
            kwargs['role_id__in'] = role_ids
        cls.objects.filter(**kwargs).delete()


class RoleMemberRel(BaseRoleMemberRel):
    role = models.ForeignKey(
        Role,
        models.RESTRICT,
        related_name='member_rels')

    class Meta:
        db_table = 'role_member_rel'
        verbose_name = '角色成员关联表'
        unique_together = ('member_id', 'role', 'member_type')
