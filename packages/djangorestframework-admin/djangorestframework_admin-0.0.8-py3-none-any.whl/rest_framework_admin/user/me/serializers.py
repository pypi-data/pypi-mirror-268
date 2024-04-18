#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/20
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from django.contrib.auth import get_user_model, password_validation
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from rest_framework_admin.user.models import User
from rest_framework_util.serializers import BaseModelSerializer


class UserModelSerializer(
        BaseModelSerializer, serializers.ModelSerializer):
    description = serializers.CharField(required=False, help_text='描述')
    nickname = serializers.CharField(required=False, help_text='昵称')
    # TODO(fengdy): 头像

    class Meta:
        model = get_user_model()
        fields = ('description', 'nickname', 'update_ts', 'update_datetime')
        read_only_fields = ('update_ts', 'update_datetime')


class UpdatePasswordUserModelSerializer(
        BaseModelSerializer, serializers.ModelSerializer):
    """ 更新密码 """
    old_password = serializers.CharField(help_text='旧密码', write_only=True)
    new_password = serializers.CharField(
        help_text='新密码',
        write_only=True, validators=[
            password_validation.validate_password])

    class Meta:
        model = User
        fields = ('old_password', 'new_password')

    def validate_old_password(self, value):
        if not self.instance.check_password(value):
            raise ValidationError(_('密码错误，请确认'))
        return value

    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password')
        instance.set_password(new_password)
        instance = super().update(instance, validated_data)
        return instance


class UpdatePhoneUserModelSerializer(
        BaseModelSerializer, serializers.ModelSerializer):
    phone = serializers.IntegerField(help_text='电话')

    class Meta:
        model = get_user_model()
        fields = ('phone', 'update_ts', 'update_datetime')
        read_only_fields = ('update_ts', 'update_datetime')


class UpdateEmailUserModelSerializer(
        BaseModelSerializer, serializers.ModelSerializer):
    email = serializers.EmailField(help_text='邮箱')

    class Meta:
        model = get_user_model()
        fields = ('email', 'update_ts', 'update_datetime')
        read_only_fields = ('update_ts', 'update_datetime')


class PartialUpdateUserModelSerializer(serializers.ModelSerializer):
    description = serializers.CharField(
        required=False, allow_blank=True, allow_null=True, help_text='描述')
    nickname = serializers.CharField(
        required=False,
        help_text='昵称')
    # TODO(fengdy): 头像

    class Meta:
        model = User
        fields = (
            'description',
            'nickname')
