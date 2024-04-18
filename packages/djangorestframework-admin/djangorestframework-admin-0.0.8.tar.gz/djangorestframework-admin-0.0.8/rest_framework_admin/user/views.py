# Create your views here.
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins
from rest_framework.decorators import action
from django.utils.translation import gettext_lazy as _

from rest_framework_admin.user import serializers
from rest_framework_admin.user.filters import UserFilter, GroupUserRelFilter
from rest_framework_admin.user.group.models import GroupUserRel
from rest_framework_admin.user.models import User
from rest_framework_admin.user.permissions import UserModelPermission, GroupUserRelModelPermission
from rest_framework_util.exceptions import HTTP403
from rest_framework_util.mixins import DestroyRelModelMixin
from rest_framework_util.viewsets import BaseModeViewSet, GenericRelViewSet, RetrieveSerializerViewSet


@extend_schema_view(
    list=extend_schema(summary='搜索用户'),
    create=extend_schema(summary='增加用户'),
    retrieve=extend_schema(summary='查询用户'),
    # update=extend_schema(summary='全量更新用户'),
    partial_update=extend_schema(summary='局部更新用户'),
    destroy=extend_schema(summary='删除用户'),
    switch=extend_schema(summary='启用、禁用用户'),
    update_password=extend_schema(summary='更新密码'),
)
class UserModelViewSet(BaseModeViewSet):
    """ 用户管理 """
    queryset = User.objects.all()
    serializer_class = serializers.UserModelSerializer
    serializer_module = serializers
    filterset_class = UserFilter
    search_fields = ['id', 'username', 'nickname', 'realname']
    ordering_fields = ['nickname', 'last_login', 'is_active']
    ordering = ['-create_datetime']
    permission_classes = (UserModelPermission,)

    def perform_destroy(self, instance):
        if instance.groups.exists():
            raise HTTP403(_('存在关联组，不允许删除'))
        instance.delete(delete_user_id=self.request.user.id)

    @action(detail=True, methods=['PATCH'], url_path='password')
    def update_password(self, request, *args, **kwargs):
        """ 修改用户密码 """
        return self.partial_update(request, *args, **kwargs)


@extend_schema_view(
    list=extend_schema(summary='搜索组'),
    destroy=extend_schema(summary='批量退出组，禁止退出自己创建的'),
)
class GroupUserRelModelViewSet(mixins.ListModelMixin,
                               DestroyRelModelMixin,
                               GenericRelViewSet):
    """ 用户关联的组管理 """
    parent_model = User
    lookup_field = 'group_id'
    queryset = GroupUserRel.objects.all()
    serializer_class = serializers.GroupUserRelModelSerializer
    serializer_module = serializers
    filterset_class = GroupUserRelFilter
    search_fields = ['group__name', 'group__description']
    ordering_fields = [
        'create_datetime',
        'group__name',
        'group__create_datetime']
    ordering = ['-create_datetime']
    permission_classes = (GroupUserRelModelPermission,)
