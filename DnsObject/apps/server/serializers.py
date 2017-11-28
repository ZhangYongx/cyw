# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Server


class ServerSerializer(serializers.ModelSerializer):
    """
        序列化 Models.Server
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    ip = serializers.IPAddressField(source='nameserver_ip', read_only=True)
    class Meta:
        model = Server
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)
        extra_kwargs = {'nameserver_ip': {'write_only': True}}

class ServerSerializer1(serializers.ModelSerializer):
    """
        序列化 Models.Server1
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Server
        fields = (
            'domain',
            'nameserver_ip',
            'nameserver_port',
            'remarks',
            'create_time',
            'update_time',
            'create_user',
            'update_user',
            'agentid'

        )
        read_only_fields = ('create_user', 'update_user',)
        extra_kwargs = {'nameserver_ip': {'write_only': True}}

class ServerSerializer2(serializers.ModelSerializer):
    """
        序列化 Models.Server2
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Server
        fields = (
            'namereverse_ip',
            'nameserver_ip',
            'nameserver_port',
            'remarks',
            'create_time',
            'update_time',
            'create_user',
            'update_user',
            'agentid'

        )
        read_only_fields = ('create_user', 'update_user',)
        extra_kwargs = {'nameserver_ip': {'write_only': True}}