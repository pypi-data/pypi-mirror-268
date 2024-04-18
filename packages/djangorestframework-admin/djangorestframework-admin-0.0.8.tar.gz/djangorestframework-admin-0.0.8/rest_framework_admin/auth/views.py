#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2024/1/2
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = []

from django.core.mail import send_mail
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import RetrieveAPIView, CreateAPIView

from rest_framework_admin import logger
from rest_framework_admin.auth.serializers import AuthMeUserModelSerializer, RegisterUserModelSerializer


@extend_schema_view(
    get=extend_schema(summary='用户自查')
)
class AuthMeRetrieveAPIView(RetrieveAPIView):
    serializer_class = AuthMeUserModelSerializer

    def get_object(self):
        return self.request.user


@extend_schema_view(
    post=extend_schema(summary='用户注册')
)
class AuthRegisterCreateAPIView(CreateAPIView):
    serializer_class = RegisterUserModelSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        try:
            send_mail(
                '【Admin】注册成功',
                f'您的账户名为{instance.username}，默认密码为，请登录更改密码！',
                None,
                [instance.email])
        except BaseException:
            logger.exception(
                f'cannot send email to registered user. email={instance.email}')
