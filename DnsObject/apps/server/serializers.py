# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Server
from PublicMethod.allserializers import AllSerializer


class ServerSerializer(AllSerializer):
    """
        序列化 Models.Server
    """
    ip = serializers.IPAddressField(source='nameserver_ip', read_only=True)

    class Meta:
        model = Server
        fields = (
            '__all__'
        )
        extra_kwargs = {'nameserver_ip': {'write_only': True}}


class ServerSerializer1(AllSerializer):
    """
        序列化 domain 字段, 当 server_method = 1 时，运行此方法。
    """

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
        extra_kwargs = {'nameserver_ip': {'write_only': True}}


class ServerSerializer2(AllSerializer):
    """
        序列化 namereverse_ip 字段, 当 server_method = 2 时，运行此方法。
    """

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
        extra_kwargs = {'nameserver_ip': {'write_only': True}}
