# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Server


class ServerSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Server
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Server
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)