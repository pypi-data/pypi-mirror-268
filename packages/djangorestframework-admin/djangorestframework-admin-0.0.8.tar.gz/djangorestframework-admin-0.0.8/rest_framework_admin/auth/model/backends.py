#!/usr/bin/python
# -*- coding:utf-8 -*-
# DateTime:2023/6/21
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['AuthBackend']

from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework.exceptions import ValidationError

UserModel = get_user_model()


class AuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        """ 主要增加异常提示以及用户是否能登录的校验 """
        # username = 'test'
        # username = 'admin'
        # password = f'{username}@2023'
        if username is None or password is None:
            return
        try:
            user = get_user_model()._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
            raise ValidationError(_('用户不存在'))
        else:
            if not user.check_password(password):
                raise ValidationError(_('密码错误'))
            if self.user_can_authenticate(user):
                return user
            return None

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False. Custom user models that don't have
        that attribute are allowed.
        """
        can = super().user_can_authenticate(user)
        return can and not user.is_deleted
