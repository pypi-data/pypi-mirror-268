#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
from django.utils.translation import gettext_lazy as _
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from rest_framework_admin.group.serializers import BaseGroupModelSerializer
from rest_framework_admin.user.configs import MemberRoleEnum
from rest_framework_admin.user.group.models import Group, GroupUserRel
from rest_framework_admin.user.models import User
from rest_framework_util.serializers import (
    BaseSwitchModelSerializer,
    BaseModelSerializer,
    BaseRelatedModelSerializer,
    BaseSelectionModelSerializer,
    BaseRelModelSerializer)


class GroupModelSerializer(BaseGroupModelSerializer):
    name = serializers.CharField(
        max_length=64, validators=[
            UniqueValidator(
                queryset=Group.objects.filter())])
    user_count = serializers.IntegerField(
        help_text='用户个数', read_only=True)

    class Meta(BaseGroupModelSerializer.Meta):
        model = Group
        fields = BaseGroupModelSerializer.Meta.fields + \
            ('user_count', )


class RelatedGroupModelSerializer(BaseRelatedModelSerializer):
    class Meta(BaseRelatedModelSerializer.Meta):
        model = GroupUserRel


class SwitchGroupModelSerializer(BaseSwitchModelSerializer):

    class Meta(BaseSwitchModelSerializer.Meta):
        model = GroupUserRel


class SelectGroupModelSerializer(BaseSelectionModelSerializer):

    class Meta(BaseSelectionModelSerializer.Meta):
        model = GroupUserRel


class GroupUserRelModelSerializer(BaseRelModelSerializer):
    id = serializers.CharField(source='user_id', read_only=True)
    name = serializers.CharField(source='user__username', read_only=True)
    role = serializers.ChoiceField(
        choices=[
            MemberRoleEnum.admin.name,
            MemberRoleEnum.member.name],
        read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = GroupUserRel
        fields = BaseModelSerializer.Meta.fields + ('role', )
        read_only_fields = fields


class CreateGroupUserRelModelSerializer(BaseRelModelSerializer):
    user_ids = serializers.ListField(
        min_length=1,
        max_length=10,
        write_only=True,
        child=serializers.PrimaryKeyRelatedField(
            queryset=User.objects.filter(
                role__in=[_.name for _ in MemberRoleEnum])))
    role = serializers.ChoiceField(
        choices=[
            MemberRoleEnum.admin.name,
            MemberRoleEnum.member.name],
        read_only=True)

    class Meta(BaseModelSerializer.Meta):
        model = GroupUserRel
        fields = BaseModelSerializer.Meta.fields + ('user_ids', 'role')
        read_only_fields = BaseModelSerializer.Meta.read_only_fields

    def create(self, validated_data):
        for user in validated_data.pop('user_ids'):
            if GroupUserRel.objects.filter(
                    user_id=user.id,
                    group_id=validated_data['group_id']).exists():
                raise ValidationError(_(f'用户【{user.name}】已加入组'))
            validated_data['user_id'] = user.id
            instance = super().create(validated_data)
        return instance


class DestroyGroupUserRelModelSerializer(BaseRelModelSerializer):
    user_ids = serializers.ListField(
        min_length=1,
        max_length=10,
        write_only=True,
        child=serializers.PrimaryKeyRelatedField(
            queryset=User.objects.filter(
                role__in=[_.name for _ in MemberRoleEnum])))

    class Meta:
        model = GroupUserRel
        fields = ('user_ids', )

    def validate_user_ids(self, users):
        user_ids = []
        group = self.context['view'].get_parent_object()
        for user in users:
            if group.user_rels.filter(user_id=user.id).exists():
                raise ValidationError(_(f'用户【{user.name}】未加入组'))
            user_ids.append(user.id)
        return user_ids
