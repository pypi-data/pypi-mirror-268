#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/20
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from django.contrib.auth import get_user_model, password_validation
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from rest_framework_admin.user.models import User
from rest_framework_util.serializers import BaseModelSerializer


class AuthMeUserModelSerializer(
        BaseModelSerializer, serializers.ModelSerializer):
    username = serializers.CharField()
    is_staff = serializers.BooleanField(
        required=False,
        default=True,
        help_text='是否为员工，默认为True')
    description = serializers.CharField(
        required=False, allow_blank=True, allow_null=True, help_text='描述')
    telephone = serializers.CharField(
        required=False, allow_blank=True, allow_null=True, help_text='电话')
    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        help_text='昵称')
    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        allow_null=True,
        help_text='邮箱')
    # avatar = ImageOrCharField(
    #     max_length=256,
    #     required=False,
    #     allow_blank=True,
    #     allow_null=True)

    class Meta:
        model = get_user_model()
        exclude = ('password', 'delete_user', 'delete_datetime')


class RegisterUserModelSerializer(
        BaseModelSerializer, serializers.ModelSerializer):
    username = serializers.CharField(
        help_text='用户名',
        validators=(
            UniqueValidator(
                queryset=User.objects.all()),))
    password = serializers.CharField(
        help_text='密码',
        write_only=True, validators=[
            password_validation.validate_password])
    email = serializers.EmailField(
        required=True,
        help_text='邮箱')

    telephone = serializers.CharField(
        required=False, allow_blank=True, allow_null=True, help_text='电话')

    nickname = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        help_text='昵称')

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'telephone', 'nickname',
                  'create_datetime')
        read_only_fields = ('id', 'create_datetime')

    def create(self, validated_data):
        if validated_data.get('is_staff', False):
            # 如果非用户，则需要管理员手动激活
            validated_data['is_active'] = False
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()
        return user
