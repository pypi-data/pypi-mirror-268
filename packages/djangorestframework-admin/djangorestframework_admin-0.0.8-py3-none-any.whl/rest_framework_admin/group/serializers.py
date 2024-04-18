#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/11/17
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from rest_framework_util.serializers import BaseModelSerializer


class BaseGroupModelSerializer(
        BaseModelSerializer, serializers.ModelSerializer):

    expire_ts = serializers.SerializerMethodField()
    expire_datetime = serializers.DateTimeField(
        input_formats='%Y%m%d%H%M', required=False)

    class Meta(BaseModelSerializer.Meta):
        fields = BaseModelSerializer.Meta.fields + \
            ('expire_datetime', 'expire_ts')

    @extend_schema_field(OpenApiTypes.INT)
    def get_expire_ts(self, obj):
        return self.get_ts_by_field(obj, 'expire_datetime')
