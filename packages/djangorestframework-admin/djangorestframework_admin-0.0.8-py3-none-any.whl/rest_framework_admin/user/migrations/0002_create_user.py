#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/21
# Tool:PyCharm

""" 创建默认用户 """
__version__ = '0.0.1'
__history__ = """"""
__all__ = []


from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import migrations

from rest_framework_admin.user.configs import DefaultUserEnum


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    # User = apps.get_model("user", "User")
    User = get_user_model()
    db_alias = schema_editor.connection.alias
    users = []
    for user_enum in DefaultUserEnum:
        users.append(
            User(
                username=user_enum.name,
                password=make_password(f"{user_enum.name}@2023"),
                **user_enum.value._asdict()))
    User.objects.using(db_alias).bulk_create(users)


def reverse_func(apps, schema_editor):
    # so reverse_func() should delete them.
    # User = apps.get_model("user", "User")
    User = get_user_model()
    db_alias = schema_editor.connection.alias
    user_ids = [_.value.id for _ in DefaultUserEnum]
    User.objects.using(db_alias).filter(id__in=user_ids).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0001_initial')
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
