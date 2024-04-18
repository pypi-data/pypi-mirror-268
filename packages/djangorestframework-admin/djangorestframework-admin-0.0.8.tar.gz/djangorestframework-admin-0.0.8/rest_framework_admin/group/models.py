#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm
from django.db import models

from rest_framework_util.db.models.base import BaseModel, BaseRelModel


class BaseGroup(BaseModel):
    expire_datetime = models.DateTimeField('过期时间', blank=True, null=True)

    class Meta:
        abstract = True


class BaseGroupMemberRel(BaseRelModel):
    expire_datetime = models.DateTimeField('过期时间', blank=True, null=True)

    class Meta:
        abstract = True
