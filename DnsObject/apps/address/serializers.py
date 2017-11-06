# -*- coding: utf-8 -*-
from rest_framework import serializers

from address import models


class AddressSerializer(serializers.ModelSerializer):
    """
        域名解析信息
    """
    #外键关联
    area_id = serializers.StringRelatedField(source='area.id')
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.Address
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)
