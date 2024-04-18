#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/21
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from enum import Enum


class MemberTypeEnum(Enum):
    user = '用户'
    group = '组'


class RoleTypeEnum(Enum):
    """ 角色类型 """
    builtin = '系统内置'
    custom = '系统自定义'
