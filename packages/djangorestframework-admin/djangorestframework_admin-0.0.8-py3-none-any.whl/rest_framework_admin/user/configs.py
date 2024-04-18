#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/21
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from enum import Enum
from typing import NamedTuple


class MemberRoleEnum(Enum):
    owner = '创建者'
    admin = '管理员'
    member = '成员'

    @classmethod
    def is_admin_or_owner(cls, name):
        return name in ['owner', 'admin']


class DefaultUserView(NamedTuple):
    id: str
    nickname: str
    role: str


class DefaultUserEnum(Enum):
    owner = DefaultUserView(
        id='0' * 32,
        nickname='超级管理员',
        role=MemberRoleEnum.owner.name)
    admin = DefaultUserView(
        id='0' * 31 + '1',
        nickname='管理员',
        role=MemberRoleEnum.admin.name)
