from django.contrib.auth import get_user_model
from django.db.models import F, Value, CharField, Q

# Create your views here.
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from rest_framework_admin.role import serializers
from rest_framework_admin.role.configs import MemberTypeEnum
from rest_framework_admin.role.filters import RoleFilter, RolePermissionRelFilter, RoleMemberRelFilter
from rest_framework_admin.role.models import Role, RolePermissionRel, RoleMemberRel
from rest_framework_admin.role.permissions import RoleModelPermission, RolePermissionRelModelPermission, \
    RoleMemberRelModelPermission, MemberListPermission
from rest_framework_admin.user.group.models import Group
from rest_framework_util.exceptions import HTTP403
from rest_framework_util.viewsets import BaseModeViewSet, BaseRelModelViewSet


@extend_schema_view(
    list=extend_schema(summary='搜索角色'),
    create=extend_schema(summary='增加角色'),
    retrieve=extend_schema(summary='查询角色'),
    partial_update=extend_schema(summary='更新角色'),
    destroy=extend_schema(summary='删除角色'),
    switch=extend_schema(summary='启用、禁用'),
    select=extend_schema(summary='搜索选择列表')
)
class RoleModelViewSet(BaseModeViewSet):
    """ 角色管理 """
    queryset = Role.objects.filter().order_by('-create_datetime').all()
    serializer_class = serializers.RoleModelSerializer
    serializer_module = serializers
    filterset_class = RoleFilter
    search_fields = ['name', 'code']
    ordering_fields = ['name', 'create_datetime']
    permission_classes = (RoleModelPermission, )

    def perform_destroy(self, instance):
        instance.delete(delete_user_id=self.request.user.id)


@extend_schema_view(
    list=extend_schema(summary='搜索权限'),
    create=extend_schema(summary='批量增加权限'),
    update=extend_schema(summary='全量更新权限'),
    destroy=extend_schema(summary='批量删除权限'),
)
class RolePermissionRelModelViewSet(BaseRelModelViewSet):
    """ 角色关联的权限管理 """
    parent_model = Role
    lookup_field = 'permission_id'
    queryset = RolePermissionRel.objects.all()
    serializer_class = serializers.RolePermissionRelModelSerializer
    filterset_class = RolePermissionRelFilter
    search_fields = ['permission__name', 'permission__description']
    ordering_fields = [
        'create_datetime',
        'permission__name',
        'permission__create_datetime']
    ordering = ['-create_datetime']
    permission_classes = (RolePermissionRelModelPermission, )


@extend_schema_view(
    list=extend_schema(summary='搜索成员'),
    create=extend_schema(summary='批量增加成员'),
    update=extend_schema(summary='全量更新成员'),
    destroy=extend_schema(summary='批量删除成员'),
)
class RoleMemberRelModelViewSet(BaseRelModelViewSet):
    """ 角色关联的成员管理 """
    parent_model = Role
    lookup_field = 'member_id'
    queryset = RoleMemberRel.objects.all()
    serializer_class = serializers.RoleMemberRelModelSerializer
    filterset_class = RoleMemberRelFilter
    search_fields = []
    ordering_fields = [
        'create_datetime',
        'type']
    ordering = ['-create_datetime']
    permission_classes = (RoleMemberRelModelPermission, )


@extend_schema_view(
    get=extend_schema(summary='搜索可赋予角色的成员列表'),
)
class MemberListAPIView(ListAPIView):
    """ 成员列表 """
    serializer_class = serializers.MemberListSerializer
    filterset_class = None
    search_fields = []
    ordering_fields = ['name', 'type']
    ordering = ['name']
    permission_classes = (MemberListPermission,)

    def get_queryset(self):
        user_queryset = get_user_model().objects.filter(is_active=True).annotate(
            name=F('username')).annotate(type=Value(MemberTypeEnum.user.name, output_field=CharField(max_length=8)))
        group_queryset = Group.objects.filter(is_active=True).annotate(
            type=Value(
                MemberTypeEnum.group.name,
                output_field=CharField(
                    max_length=8)))
        name = self.request.query_params.get('name', None) or None
        if not name:
            name = self.request.query_params.get('search', None) or None
        if name is not None:
            user_queryset = user_queryset.filter(Q(realname__icontains=name) | Q(
                nickname__icontains=name) | Q(username__icontains=name))
            group_queryset = group_queryset.filter(name__icontains=name)

        keys = [
            'id',
            'is_active',
            'description',
            'create_datetime',
            'name',
            'type']
        user_queryset = user_queryset.values(*keys)
        group_queryset = group_queryset.values(*keys)
        member_type = self.request.query_params.get('type', None) or None
        if member_type == MemberTypeEnum.user.name:
            return user_queryset
        elif member_type == MemberTypeEnum.group.name:
            return group_queryset
        else:
            queryset = user_queryset.union(
                group_queryset, all=True)
        return queryset
