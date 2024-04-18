# Create your views here.
from drf_spectacular.utils import extend_schema_view, extend_schema
from django.utils.translation import gettext_lazy as _
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework_admin.tenant import serializers
from rest_framework_admin.tenant.filters import TenantFilter, TenantUserRelFilter
from rest_framework_admin.tenant.models import Tenant, TenantUserRel
from rest_framework_admin.tenant.permissions import TenantModelPermission, TenantUserRelModelPermission
from rest_framework_admin.tenant.serializers import TenantModelSerializer
from rest_framework_util.exceptions import HTTP403
from rest_framework_util.mixins import CreateRelModelMixin, DestroyRelModelMixin
from rest_framework_util.viewsets import BaseModeViewSet, BaseRelModelViewSet, GenericRelViewSet


@extend_schema_view(
    switch=extend_schema(summary='启用、禁用'),
)
class TenantModelViewSet(BaseModeViewSet):
    """ 租户管理 """
    queryset = Tenant.objects.filter().order_by('-create_datetime').all()
    serializer_class = TenantModelSerializer
    serializer_module = serializers
    filterset_class = TenantFilter
    search_fields = ['id', 'name']
    ordering_fields = ['name', 'create_datetime']
    permission_classes = (TenantModelPermission,)

    def perform_destroy(self, instance):
        instance.delete(delete_user_id=self.request.user.id)


@extend_schema_view(
    list=extend_schema(summary='搜索用户'),
    create=extend_schema(summary='批量增加用户'),
    destroy=extend_schema(summary='批量删除用户'),
)
class TenantUserRelModelViewSet(mixins.ListModelMixin,
                                CreateRelModelMixin,
                                DestroyRelModelMixin,
                                GenericRelViewSet):
    """ 关联的用户管理 """
    parent_model = Tenant
    lookup_field = 'user_id'
    queryset = TenantUserRel.objects.all()
    serializer_class = serializers.TenantUserRelModelSerializer
    filterset_class = TenantUserRelFilter
    search_fields = ['user__username', 'user__nickname']
    ordering_fields = [
        'create_datetime',
        'user__username',
        'user__create_datetime']
    ordering = ['-create_datetime']
    permission_classes = (TenantUserRelModelPermission,)
