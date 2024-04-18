# Create your views here.

from django.contrib.auth.models import AnonymousUser
from django.core.cache import cache
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.response import Response
from rest_framework.status import is_success
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework_admin.auth.jwt.utils import blacklist


@extend_schema_view(
    post=extend_schema(summary='登出', responses=OpenApiTypes.NONE)
)
class LogoutAPIView(APIView):
    def post(self, request, *args, **kwargs):
        response = Response({})
        if not isinstance(request.user, AnonymousUser):
            blacklist.add_by_user(request.user)
        return response


class TokenCacheApiView:
    @staticmethod
    def set_cache(request, response, data=None):
        data = data or response.data or {}
        cache_data = {}
        for token_key, token_class in (
                ('access', AccessToken),
                ('refresh', RefreshToken)):
            value = data.get(token_key, None)
            if value:
                cache_data[token_key] = token_class(value).payload['jti']
        cache.set(request.user.id, cache_data)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if is_success(response.status_code):
            self.set_cache(request, response)
        return response


@extend_schema_view(
    post=extend_schema(summary='登入')
)
class LoginAPIView(TokenCacheApiView, TokenObtainPairView):
    pass


@extend_schema_view(
    post=extend_schema(summary='刷新token')
)
class RefreshAPIView(TokenCacheApiView, TokenRefreshView):
    pass
