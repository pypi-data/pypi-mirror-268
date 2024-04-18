#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/21
# Tool:PyCharm

""" 删除无用表 """
__version__ = '0.0.1'
__history__ = """"""
__all__ = []


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_role', '0001_initial'),
    ]

    operations = [
        # FIXME(fengdy): auth模块会发出信号，信号接收者会使用如下表
        # migrations.RunSQL('DROP TABLE IF EXISTS auth_group_permissions;'),
        # migrations.RunSQL('DROP TABLE IF EXISTS auth_group;'),
        # migrations.RunSQL('DROP TABLE IF EXISTS auth_permission;'),
        # migrations.RunSQL('DROP TABLE IF EXISTS django_admin_log;'),
        # migrations.RunSQL('DROP TABLE IF EXISTS django_content_type;'),
    ]
