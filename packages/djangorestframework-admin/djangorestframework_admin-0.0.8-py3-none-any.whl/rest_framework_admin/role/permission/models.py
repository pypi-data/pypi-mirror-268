#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm

from django.db import models
from rest_framework_util.db.models.base import BaseModel, BaseRelModel


class BasePermission(BaseModel):
    content_type = models.CharField('内容类型', max_length=64)
    action = models.CharField('动作', max_length=64)

    class Meta:
        abstract = True

    def extended_strs(self):
        return [f'content_type={self.content_type}', f'action={self.action}']


class Permission(BasePermission):

    class Meta:
        db_table = 'role_permission'
        verbose_name = '权限表'
        unique_together = ('content_type', 'action')
