#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2024/3/25
from django.conf import settings
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework_util.decorators import login_exempt

if settings.DEBUG:
    urlpatterns = [
        path(
            'schema/',
            login_exempt(SpectacularAPIView.as_view()), name='schema'),
        path(
            'schema/swagger-ui/',
            login_exempt(SpectacularSwaggerView.as_view(url_name='schema')), name='swagger-ui'),
        path(
            'schema/redoc/',
            login_exempt(SpectacularRedocView.as_view(url_name='schema')), name='redoc'),
    ]
else:
    urlpatterns = []
