# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Host


class HostSerializer(serializers.ModelSerializer):
    """
    序列化 Models.HostRecord
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    ip = serializers.IPAddressField(source='host_ip', read_only=True)
    class Meta:
        model = Host
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)
        extra_kwargs = {'host_ip': {'write_only': True}}