# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Host


class HostSerializer(serializers.ModelSerializer):
    """
    序列化 Models.HostRecord
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Host
        fields = (
            '__all__'
        )
        read_only_field = ('create_user', 'update_user',)

