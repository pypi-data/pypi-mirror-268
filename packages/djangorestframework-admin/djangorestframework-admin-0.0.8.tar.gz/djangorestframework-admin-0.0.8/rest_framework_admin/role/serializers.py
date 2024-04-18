#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from rest_framework_admin.role.configs import RoleTypeEnum, MemberTypeEnum
from rest_framework_admin.role.models import Permission
from rest_framework_admin.role.models import Role, RoleMemberRel, RolePermissionRel
from rest_framework_admin.user.group.models import Group
from rest_framework_admin.user.serializers import UserModelSerializer
from rest_framework_util.serializers import BaseModelSerializer, RelatedUserModelSerializer, BaseSwitchModelSerializer, \
    BaseSelectionModelSerializer, BaseRelModelSerializer


class RoleModelSerializer(BaseModelSerializer):
    type = serializers.ChoiceField(
        [RoleTypeEnum.custom.name])
    name = serializers.CharField(max_length=64)
    code = serializers.CharField(max_length=64)
    member_count = serializers.SerializerMethodField(help_text='主体个数统计')
    weight = serializers.IntegerField(
        required=False,
        help_text='权重，值越高优先级越高，即权限越大',
        min_value=1,
        max_value=100)

    class Meta(BaseModelSerializer.Meta):
        model = Role
        fields = BaseModelSerializer.Meta.fields + \
            ('code', 'member_count', 'type', 'weight')
        validators = []

    @extend_schema_field({'type': 'object',
                          'properties': {'all': {'type': 'int',
                                                 'description': '所有主体个数'},
                                         '{key}': {'type': 'int',
                                                   'description': '个数,{key}为主体类型'}}})
    def get_member_count(self, obj):
        data = {'all': obj.member_rels.count()}
        for enum in MemberTypeEnum:
            data[enum.name] = obj.member_rels.filter(
                member_type=enum.name).count()
        return data


class RelatedRoleMemberRelModelSerializer(BaseRelModelSerializer):
    """ 关联的角色 """
    id = serializers.CharField(source='role_id', read_only=True)
    code = serializers.SlugRelatedField(
        source='role', slug_field='code', read_only=True)
    name = serializers.SlugRelatedField(
        source='role', slug_field='name', read_only=True)
    create_user = RelatedUserModelSerializer(help_text='绑定用户与角色的人员')

    class Meta(BaseRelModelSerializer.Meta):
        model = RoleMemberRel
        fields = BaseRelModelSerializer.Meta.fields + ('code', 'name')


class SwitchRoleModelSerializer(BaseSwitchModelSerializer):

    class Meta(BaseSwitchModelSerializer.Meta):
        model = Role


class SelectRoleModelSerializer(BaseSelectionModelSerializer):
    class Meta(BaseSelectionModelSerializer.Meta):
        model = Role
        fields = BaseSelectionModelSerializer.Meta.fields + ('type', )


class RolePermissionRelModelSerializer(BaseRelModelSerializer):
    id = serializers.CharField(source='permission_id')
    name = serializers.CharField(source='permission__name')

    class Meta(BaseRelModelSerializer.Meta):
        model = RolePermissionRel
        fields = BaseRelModelSerializer.Meta.fields + ('id', 'name')


class CreateRolePermissionRelModelSerializer(BaseRelModelSerializer):
    permission_ids = serializers.ListField(
        min_length=1,
        max_length=10,
        write_only=True,
        child=serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all()))

    class Meta:
        model = RolePermissionRel
        fields = ('permission_ids', )

    def create(self, validated_data):
        for permission in validated_data.pop('permission_ids'):
            if RolePermissionRel.objects.filter(
                    permission_id=permission.id,
                    role_id=validated_data['role_id']).exists():
                raise ValidationError(_(f'权限【{permission.name}】已关联'))
            validated_data['permission_id'] = permission.id
            instance = super().create(validated_data)
        return instance


class RoleMemberRelModelSerializer(BaseRelModelSerializer):
    id = serializers.CharField(source='member_id')
    type = serializers.ChoiceField(
        [enum.name for enum in MemberTypeEnum], source='member_type')
    name = serializers.SerializerMethodField()
    member_ids = serializers.ListField(
        min_length=1,
        max_length=10,
        write_only=True,
        child=serializers.CharField(max_length=32, min_length=32))

    class Meta(BaseRelModelSerializer.Meta):
        model = RoleMemberRel
        fields = BaseRelModelSerializer.Meta.fields + ('member_ids', )

    def get_name(self, obj):
        return obj.member.name

    def create(self, validated_data):
        member_type = validated_data['type']
        for member_id in validated_data.pop('member_ids'):
            if member_type == MemberTypeEnum.group.name:
                enum = MemberTypeEnum.group
                model = Group
            else:
                enum = MemberTypeEnum.user
                model = get_user_model()
            if not model.objects.filter(pk=member_id).exists():
                raise ValidationError(
                    _(f'[{enum.value}]类型实体[id={member_id}]不存在'))
            if not RoleMemberRel.objects.filter(
                    member_id=member_id,
                    member_type=member_type,
                    role_id=validated_data['role_id']).exists():
                validated_data['member_id'] = member_id
                instance = super().create(validated_data)
        return instance


# ========== 主体 ==========


class MemberListSerializer(serializers.Serializer):
    id = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField()
    type = serializers.CharField()
    create_ts = serializers.SerializerMethodField()
    #
    username = serializers.SerializerMethodField()
    nickname = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()
    last_login_ts = serializers.SerializerMethodField()
    expire_ts = serializers.SerializerMethodField()
    role = serializers.SerializerMethodField()
    #
    name = serializers.SerializerMethodField()
    user_count = serializers.SerializerMethodField()
    create_datetime = serializers.DateTimeField()

    class Meta:
        fields = list(set([
            'id',
            'type',

            # user类型
            'username',
            'nickname',
            'is_active',
            'last_login',
            'last_login_ts',
            'expire_ts'
            'description',

            # group类型
            'name',
            'description',
            'user_count',
            'create_ts']))

    def __get_obj(self, obj):
        key = '_obj_instance__'
        if key not in obj:
            if obj["type"] == MemberTypeEnum.user.name:
                model = get_user_model()
            else:
                model = Group
            obj[key] = model.objects.get(pk=obj["id"])
        return obj[key]

    def get_create_ts(self, obj):
        instance = self.__get_obj(obj)
        return BaseModelSerializer().get_create_ts(instance)

    def get_username(self, obj):
        instance = self.__get_obj(obj)
        return getattr(instance, 'username', None)

    def get_name(self, obj):
        instance = self.__get_obj(obj)
        return getattr(instance, 'name', None)

    def get_nickname(self, obj):
        instance = self.__get_obj(obj)
        return getattr(instance, 'nickname', None)

    def get_last_login(self, obj):
        instance = self.__get_obj(obj)
        return getattr(instance, 'last_login', None)

    def get_last_login_ts(self, obj):
        instance = self.__get_obj(obj)
        return BaseModelSerializer().get_ts_by_field(instance, 'last_login')

    def get_user_count(self, obj):
        instance = self.__get_obj(obj)
        return getattr(instance, 'user_count', None)

    def get_expire_ts(self, obj):
        instance = self.__get_obj(obj)
        return getattr(instance, 'expire_ts', None)

    def get_role(self, obj):
        instance = self.__get_obj(obj)
        if obj['type'] == MemberTypeEnum.user.name:
            return UserModelSerializer(context=self.context).get_role(instance)
        return None
