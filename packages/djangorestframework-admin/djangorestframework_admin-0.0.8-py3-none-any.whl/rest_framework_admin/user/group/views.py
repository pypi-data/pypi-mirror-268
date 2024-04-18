# Create your views here.
from drf_spectacular.utils import extend_schema_view, extend_schema
from django.utils.translation import gettext_lazy as _

from rest_framework_admin.user.group import serializers
from rest_framework_admin.user.group.filters import GroupFilter, GroupUserRelFilter
from rest_framework_admin.user.group.models import Group, GroupUserRel
from rest_framework_admin.user.group.permissions import GroupModelPermission, GroupUserRelModelPermission
from rest_framework_admin.user.group.serializers import GroupModelSerializer
from rest_framework_util.exceptions import HTTP403
from rest_framework_util.viewsets import BaseModeViewSet, BaseRelModelViewSet


@extend_schema_view(
    switch=extend_schema(summary='启用、禁用'),
)
class GroupModelViewSet(BaseModeViewSet):
    """ 组管理 """
    queryset = Group.objects.filter().order_by('-create_datetime').all()
    serializer_class = GroupModelSerializer
    serializer_module = serializers
    filterset_class = GroupFilter
    search_fields = ['name']
    ordering_fields = ['name', 'create_datetime']
    permission_classes = (GroupModelPermission,)

    def get_queryset(self):
        if self.request.user.is_admin_or_owner:
            queryset = super().get_queryset()
        else:
            queryset = self.request.user.groups
        return queryset

    def perform_destroy(self, instance):
        # TODO(fengdy): 关联角色限制
        instance.delete(delete_user_id=self.request.user.id)


@extend_schema_view(
    list=extend_schema(summary='搜索用户'),
    create=extend_schema(summary='批量增加用户'),
    update=extend_schema(summary='全量更新用户'),
    destroy=extend_schema(summary='批量删除用户'),
)
class GroupUserRelModelViewSet(BaseRelModelViewSet):
    """ 组关联的用户管理 """
    parent_model = Group
    lookup_field = 'user_id'
    queryset = GroupUserRel.objects.all()
    serializer_class = serializers.GroupUserRelModelSerializer
    serializer_module = serializers
    filterset_class = GroupUserRelFilter
    search_fields = ['user__username', 'user__nickname']
    ordering_fields = [
        'create_datetime',
        'user__username',
        'user__create_datetime']
    ordering = ['-create_datetime']
    permission_classes = (GroupUserRelModelPermission,)
