#!/usr/bin/python
# -*- coding:utf-8 -*-
# DateTime:2023/6/21
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = ['RefreshSerializer', 'TokenSerializer', 'OauthLogoutSerializer']

from rest_framework import serializers, exceptions
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _

from rest_framework_admin.auth.jwt.exceptions import AuthVerifyError
from rest_framework_admin.auth.jwt.utils import blacklist


class BlacklistRefreshToken(RefreshToken):
    def verify(self, *args, **kwargs) -> None:
        super().verify(*args, **kwargs)
        self.check_blacklist()

    def check_blacklist(self):
        if blacklist.has_token(self):
            raise TokenError(_("Token has no id"))


class RefreshSerializer(TokenRefreshSerializer):
    """
    调整 `refresh` 为非必填项，此时通过COOKIE获取
    """
    token_class = BlacklistRefreshToken


class TokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            return super().validate(attrs)
        except exceptions.AuthenticationFailed as exc:
            raise AuthVerifyError(_('认证失败，未找到有效用户'))


class OauthLogoutSerializer(serializers.Serializer):
    grant_type = serializers.ChoiceField(choices=['logout'])
    refresh_token = serializers.CharField(max_length=256)
    client_id = serializers.CharField(max_length=256)
    client_secret = serializers.CharField(max_length=256)
