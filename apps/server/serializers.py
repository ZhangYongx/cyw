# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Server
from rest_framework import serializers


class ServerSerializer(AllSerializer):
    """
    序列化 Models.Server。
    domain 与 reverse_ip 同时仅共存一个
    """
    ip = serializers.IPAddressField(source='nameserver_ip', read_only=True)

    class Meta:
        model = Server
        fields = '__all__'
        extra_kwargs = {'nameserver_ip': {"write_only": True}}


class ServerSerializer1(serializers.ModelSerializer):
    """
    序列化1：仅序列化 domain
    """
    class Meta:
        model = Server
        fields = (
            'domain',
            'nameserver_ip',
            'nameserver_port',
            'agt_id',
            'create_time',
            'update_time',
            'create_user',
            'update_user',
            'remarks',
        )
        extra_kwargs = {'nameserver_ip': {"write_only": True}}


class ServerSerializer2(serializers.ModelSerializer):
    """
    序列化2：仅序列化 nsreverse_ip
    """
    model = Server
    fields = (
        'nsreverse_ip',
        'nameserver_ip',
        'nameserver_port',
        'agt_id',
        'create_time',
        'update_time',
        'create_user',
        'update_user',
        'remarks',
    )
    extra_kwargs = {'nameserver_ip': {"write_only": True}}
