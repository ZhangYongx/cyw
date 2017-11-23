# -*- coding: utf-8 -*-
from rest_framework import serializers

from address import models


class AddressSerializer(serializers.ModelSerializer):
    """
        域名解析信息
    """
    #外键关联
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    ip = serializers.IPAddressField(source='addr_ip', read_only=True)
    class Meta:
        model = models.Address
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)
