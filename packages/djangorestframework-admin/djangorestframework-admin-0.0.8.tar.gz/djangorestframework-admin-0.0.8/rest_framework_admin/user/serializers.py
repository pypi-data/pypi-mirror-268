#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator

from rest_framework_admin.user.configs import MemberRoleEnum
from rest_framework_admin.user.group.models import Group
from rest_framework_admin.user.models import User, GroupUserRel
from rest_framework_util.serializers import BaseSwitchModelSerializer, BaseModelSerializer, BaseSelectionModelSerializer, BaseRelModelSerializer


class UserModelSerializer(BaseModelSerializer):
    username = serializers.CharField(
        write_only=True,
        help_text='账户（不允许更新）',
        validators=(
            UniqueValidator(
                queryset=User.objects.filter()),))
    password = serializers.CharField(
        help_text='密码（不允许更新）',
        write_only=True, validators=[
            password_validation.validate_password])
    is_active = serializers.BooleanField(
        required=False,
        default=True,
        help_text='是否激活，默认为True')
    description = serializers.CharField(
        required=False, allow_blank=True, allow_null=True, help_text='描述')
    phone = serializers.CharField(
        required=False,
        write_only=True,
        help_text='电话')
    name = serializers.CharField(read_only=True)
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
    role = serializers.ChoiceField(
        [_.name for _ in MemberRoleEnum], default=None, required=False, allow_null=True)
    # avatar = ImageOrCharField(
    #     max_length=256,
    #     required=False,
    #     allow_blank=True,
    #     allow_null=True)
    # TODO(fengdy): 头像
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        read_only_fields = ('create_datetime', 'id', 'last_login', 'is_staff')
        exclude = ('delete_user', 'delete_datetime')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()
        return user


class PartialUpdateUserModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
        validators=(
            UniqueValidator(
                queryset=User.objects.filter()),),
        write_only=True)
    role = serializers.ChoiceField(
        [MemberRoleEnum.admin.name, MemberRoleEnum.member.name],
        required=False)
    description = serializers.CharField(
        required=False, allow_blank=True, allow_null=True, help_text='描述')
    phone = serializers.CharField(
        required=False,
        help_text='电话')
    nickname = serializers.CharField(
        required=False,
        help_text='昵称')
    email = serializers.EmailField(
        required=False,
        help_text='邮箱')
    # TODO(fengdy): 头像

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'description',
            'nickname',
            'phone',
            'email',
            'role')

    def validate_role(self, value):
        if not self.instance.is_staff:
            raise ValidationError(_('仅允许内部员工更新'))
        return value


class SwitchUserModelSerializer(BaseSwitchModelSerializer):

    class Meta(BaseSwitchModelSerializer.Meta):
        model = User


class UpdatePasswordUserModelSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(
        help_text='新密码',
        write_only=True, validators=[
            password_validation.validate_password])

    class Meta:
        model = User
        fields = ('new_password', )

    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password')
        instance.set_password(new_password)
        instance = super().update(instance, validated_data)
        return instance


class SelectUserModelSerializer(BaseSelectionModelSerializer):

    class Meta(BaseSelectionModelSerializer.Meta):
        model = User


class GroupUserRelModelSerializer(BaseRelModelSerializer):
    id = serializers.CharField(source='group_id', read_only=True)
    name = serializers.CharField(source='group__name', read_only=True)

    class Meta(BaseRelModelSerializer.Meta):
        model = GroupUserRel


class DestroyGroupUserRelModelSerializer(BaseRelModelSerializer):
    group_ids = serializers.ListField(
        min_length=1,
        max_length=10,
        write_only=True,
        child=serializers.PrimaryKeyRelatedField(queryset=Group.objects.all()))

    class Meta:
        model = GroupUserRel
        fields = ('group_ids', )

    def validate_group_ids(self, groups):
        group_ids = []
        user = self.context['view'].get_parent_object()
        for group in groups:
            rel = user.group_rels.filter(group_id=group.id).first()
            if not rel:
                raise ValidationError(_(f'用户未加入组【{group.name}】'))
            if rel.role == MemberRoleEnum.owner.name:
                raise ValidationError(_(f'当前角色为组【{group.name}】创建者，禁止退出'))
            group_ids.append(group.id)
        return group_ids
