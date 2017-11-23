# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Alias
from IPy import IP


class AliasSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Alias
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Alias
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)


class AliasSerializer1(serializers.ModelSerializer):
    """
    序列化 Models.Alias
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Alias
        fields = (
            'start_ip',
            'end_ip',
            'new_ip',
            'ipmask',
            'create_time',
            'update_time',
            'create_user',
            'update_user',
            'agentid',
            'remarks'
        )
        read_only_fields = ('create_user', 'update_user',)


class AliasSerializer2(serializers.ModelSerializer):

    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Alias
        fields = (
            'old_ip',
            'new_ip',
            'ipmask',
            'create_time',
            'update_time',
            'create_user',
            'update_user',
            'agentid',
            'remarks'
        )
        read_only_fields = ('create_user', 'update_user',)

