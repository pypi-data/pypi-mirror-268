#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/16
# Tool:PyCharm
__all__ = ['Config']

from django.db import models

from rest_framework_util.db.models.base import BaseModel


class Config(BaseModel):
    value = models.TextField('值', null=True, blank=True)

    class Meta:
        db_table = 'system_config'
        verbose_name = '系统配置表'
