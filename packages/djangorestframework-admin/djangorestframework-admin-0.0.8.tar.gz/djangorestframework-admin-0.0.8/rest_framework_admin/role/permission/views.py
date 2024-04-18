# Create your views here.
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import viewsets

from rest_framework_admin.role.permission.filters import PermissionFilter
from rest_framework_admin.role.permission.models import Permission
from rest_framework_admin.role.permission.permissions import PermissionModelPermission
from rest_framework_admin.role.permission.serializers import PermissionModelSerializer


@extend_schema_view(
    list=extend_schema(summary='搜索权限'),
    retrieve=extend_schema(summary='查询权限'),
)
class PermissionModelViewSet(viewsets.ReadOnlyModelViewSet):
    """ 权限管理 """
    queryset = Permission.objects.filter().order_by('-create_datetime').all()
    serializer_class = PermissionModelSerializer
    filterset_class = PermissionFilter
    search_fields = ['name']
    ordering_fields = ['name', 'create_datetime']
    permission_classes = (PermissionModelPermission, )
