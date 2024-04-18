#!/usr/bin/python
# -*- coding:utf-8 -*-
# Email:iamfengdy@126.com
# DateTime:2023/10/10
# Tool:PyCharm

"""  """
__version__ = '0.0.1'
__history__ = """"""
__all__ = [
    'ListConfigModelSerializer',
    'UpdateConfigModelSerializer'
]

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from rest_framework_admin.system.models import Config


class ListConfigModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text='名称')
    value = serializers.CharField(help_text='值', source='decrypted_value')

    class Meta:
        model = Config
        fields = ('name', 'value')
        read_only_fields = fields


class UpdateConfigModelSerializer(serializers.Serializer):
    values = serializers.DictField(
        child=serializers.CharField(allow_blank=True),
        help_text='键值对，key为名称，value为值')

    def create(self, validated_data):
        user_id = validated_data['update_user_id']
        for name, value in validated_data['values'].items():
            try:
                instance = Config.objects.get(name=name)
            except Config.DoesNotExist:
                instance = Config(name=name, create_user_id=user_id)
            except BaseException:
                raise ValidationError('name错误')
            instance.update_user_id = user_id
            instance.value = value
            instance.save()
        return []

    def update(self, instance, validated_data):
        return []
