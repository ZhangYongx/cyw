# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import *


class DNSUserSerializer(serializers.ModelSerializer):
    """
    序列化 Models.UserTable
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = DNSUser
        fields = (
            '__all__'
        )


class AreaSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Area
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Area
        fields = (
            '__all__'
        )


class AgentSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Agent
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    # # 实现 create() 方法
    # def create(self, validated_data):
    #     return Agent(**validated_data)
    # #
    # # 实现 update() 方法
    # def update(self, instance, validated_data):
    #     instance.agtIP = validated_data.get('agtIP', instance.agtIP)
    #     instance.agtVersion = validated_data.get('agtVersion', instance.agtVersion)
    #     instance.agtStates = validated_data.get('agtStates', instance.agtStates)
    #     instance.remark = validated_data.get('remark', instance.remark)
    #     return instance

    class Meta:
        model = Agent
        fields = (
            '__all__'
        )


class LocalSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Local
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Local
        fields = (
            '__all__'
        )


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


class AddressSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Address
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    addressIP = serializers.IPAddressField()

    class Meta:
        model = Address
        fields = (
            '__all__'
        )


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


class PtrSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Ptr
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Ptr
        fields = (
            '__all__'
        )


class SrvSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Srv
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Srv
        fields = (
            '__all__'
        )


class MxSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Mx
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Mx
        fields = (
            '__all__'
        )


class TxtSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Txt
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Txt
        fields = (
            '__all__'
        )


class CnameSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Cname
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Cname
        fields = (
            '__all__'
        )


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


class ResolvSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Resolv
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Resolv
        fields = (
            '__all__'
        )


class IPinfoSerializer(serializers.ModelSerializer):
    """
    Serializer Models.IP
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = IPinfo
        fields = (
            '__all__'
        )


class TopDomainSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Domain
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = TopDomain
        fields = (
            '__all__'
        )


class SecondDomainSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Domain
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = SecondDomain
        fields = (
            '__all__'
        )


