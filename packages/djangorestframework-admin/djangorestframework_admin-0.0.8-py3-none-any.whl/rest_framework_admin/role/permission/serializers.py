#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from rest_framework_admin.role.permission.models import Permission
from rest_framework_util.serializers import BaseModelSerializer


class PermissionModelSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Permission
