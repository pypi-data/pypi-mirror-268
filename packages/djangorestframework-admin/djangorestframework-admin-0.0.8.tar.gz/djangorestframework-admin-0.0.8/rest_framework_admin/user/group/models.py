#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm
from django.contrib.auth import get_user_model
from django.db import models

from rest_framework_admin.user.configs import MemberRoleEnum
from rest_framework_util.db.models.base import BaseModel, BaseRelModel


class Group(BaseModel):
    users = models.ManyToManyField(
        get_user_model(), through='GroupUserRel', through_fields=(
            'group', 'user'), related_name='groups')
    expire_datetime = models.DateTimeField('过期时间', blank=True, null=True)

    class Meta:
        db_table = 'user_group'
        verbose_name = '用户组表'

    @property
    def user_count(self):
        return self.user_rels.count()


class GroupUserRel(BaseRelModel):
    user = models.ForeignKey(
        get_user_model(),
        models.CASCADE,
        related_name='group_rel')
    group = models.ForeignKey(Group, models.CASCADE, related_name='user_rel')
    role = models.CharField(
        max_length=32,
        choices=[
            (_.name,
             _.value) for _ in MemberRoleEnum],
        default=MemberRoleEnum.member.name)

    class Meta:
        db_table = 'user_group_user_rel'
        verbose_name = '用户组关联表'
        unique_together = ('user', 'group', 'delete_datetime')

    def extended_strs(self):
        return [f'user_id={self.user.id}', f'group_id={self.group.id})']
