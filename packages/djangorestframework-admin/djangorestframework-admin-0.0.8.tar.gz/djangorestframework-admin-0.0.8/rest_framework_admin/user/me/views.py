# Create your views here.
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from rest_framework_admin.user.me import serializers
from rest_framework_admin.user.me.serializers import PartialUpdateUserModelSerializer
from rest_framework_admin.user.models import User
from rest_framework_util.viewsets import RetrieveSerializerViewSet


@extend_schema_view(
    # update=extend_schema(summary='全量更新'),
    # partial_update=extend_schema(summary='局部更新'),
    update_password=extend_schema(summary='更新密码'),
    update_email=extend_schema(summary='更新邮箱'),
    update_phone=extend_schema(summary='更新电话'),
)
class MeModelViewSet(RetrieveSerializerViewSet,
                     GenericViewSet):
    """ 用户 """
    queryset = User.objects.all()
    serializer_class = serializers.UserModelSerializer
    serializer_module = serializers

    def get_object(self):
        return self.request.user

    @action(detail=False, methods=['PATCH'], url_path='password')
    def update_password(self, request, *args, **kwargs):
        """ 重置密码 """
        return self.partial_update(request, *args, **kwargs)

    @action(detail=False, methods=['PATCH'], url_path='email')
    def update_email(self, request, *args, **kwargs):
        """ 用户修改自己的密码 """
        return self.partial_update(request, *args, **kwargs)

    @action(detail=False, methods=['PATCH'], url_path='phone')
    def update_phone(self, request, *args, **kwargs):
        """ 更新电话 """
        return self.partial_update(request, *args, **kwargs)


@extend_schema_view(
    patch=extend_schema(summary='用户更新'),
)
class UpdateUserModelApiView(GenericAPIView):
    serializer_class = PartialUpdateUserModelSerializer

    def get_queryset(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()
