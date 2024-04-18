# Create your views here.
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_admin.system.filters import ConfigFilter
from rest_framework_admin.system.models import Config
from rest_framework_admin.system.permissions import ConfigPermission
from rest_framework_admin.system.serializers import ListConfigModelSerializer, UpdateConfigModelSerializer
from rest_framework_admin.system.settings import api_settings
from rest_framework_util.core.upload import FileView
from rest_framework_util.viewsets import BaseFileUploadAPIView


@extend_schema_view(
    get=extend_schema(
        summary='系统配置/列表', parameters=[
            OpenApiParameter('name', description='多个值英文逗号分隔')]),
    put=extend_schema(summary='系统配置/更新'),
    patch=extend_schema(summary='系统配置/更新')
)
class SysConfigAPIView(ListAPIView, UpdateAPIView):
    queryset = Config.objects.all()
    pagination_class = None
    serializer_class = ListConfigModelSerializer
    filterset_class = ConfigFilter
    search_fields = ['name']
    ordering_fields = ['name', 'create_datetime', 'update_datetime']
    ordering = ['-create_datetime']
    permission_classes = (ConfigPermission,)

    def get_serializer_class(self):
        if self.request.method != 'GET':
            return UpdateConfigModelSerializer
        return self.serializer_class

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(update_user_id=request.user.id)
        return Response({})


@extend_schema_view(
    post=extend_schema(
        summary='文件/上传',
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'file': {'type': 'string', 'format': 'binary', 'description': '文件'},
                    'type': {'type': 'string', 'description': '类型'},
                    'uuid': {'type': 'string', 'description': '分片时，用于文件唯一标识；不分片就不用'},
                    'task_id': {'type': 'string', 'description': '文件id，用于生成文件夹名称'},
                    'chunk': {'type': 'int', 'description': '分片序号，-1表示部不分片'}
                },
                'required': ['file', 'type', 'uuid', 'task_id']
            }},
    ),
)
class FileUploadAPIView(BaseFileUploadAPIView):
    app_settings = api_settings.UPLOAD_SETTINGS

    def get_file_view(self, request):
        file_view = FileView(file_type=request.data.get('type', 'file'),
                             file_id=request.data['uuid'],
                             dir_path=self.get_dir_path(request),
                             task_id=request.data['task_id'],
                             chunk=request.data.get('chunk', -1),
                             file_name=None)
        return file_view


@extend_schema_view(
    post=extend_schema(
        summary='文件/合并（只针对分片上传的文件）',
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'filename': {'type': 'string', 'description': '文件名称'},
                    'type': {'type': 'string', 'description': '类型'},
                    'uuid': {'type': 'string', 'description': '用于文件唯一标识'},
                    'task_id': {'type': 'string', 'description': '文件id，用于生成文件夹名称'}
                },
                'required': ['filename', 'type', 'uuid', 'task_id']
            }}, ),
)
class FileMergeAPIView(BaseFileUploadAPIView):
    app_settings = api_settings.UPLOAD_SETTINGS

    def get_file_view(self, request):
        file_view = FileView(file_type=request.data.get('type', 'file'),
                             file_id=request.data['uuid'],
                             dir_path=self.get_dir_path(request),
                             task_id=request.data['task_id'],
                             chunk=None,
                             file_name=request.data['filename'])
        return file_view
