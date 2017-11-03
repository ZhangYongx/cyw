# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import *


class UserTableSerializer(serializers.ModelSerializer):
    """
    序列化 Models.UserTable
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = UserTable
        fields = (
            '__all__'
        )


class AreaSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Area
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Area
        fields = (
            '__all__'
        )


class AgentSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Agent
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

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
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Local
        fields = (
            '__all__'
        )


class ServerSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Server
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Server
        fields = (
            '__all__'
        )


class AddressSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Address
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Address
        fields = (
            '__all__'
        )


class HostRecordSerializer(serializers.ModelSerializer):
    """
    序列化 Models.HostRecord
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = HostRecord
        fields = (
            '__all__'
        )


class PtrSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Ptr
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Ptr
        fields = (
            '__all__'
        )


class SrvSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Srv
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Srv
        fields = (
            '__all__'
        )


class MxSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Mx
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Mx
        fields = (
            '__all__'
        )


class TxtSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Txt
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Txt
        fields = (
            '__all__'
        )


class CnameSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Cname
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Cname
        fields = (
            '__all__'
        )


class AliasSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Alias
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Alias
        fields = (
            '__all__'
        )


class ResolvSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Resolv
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Resolv
        fields = (
            '__all__'
        )


class MachineRoomSerializer(serializers.ModelSerializer):
    """
    Serializer Models.MachineRoom
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = MachineRoom
        fields = (
            '__all__'
        )


class IPSerializer(serializers.ModelSerializer):
    """
    Serializer Models.IP
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = IP
        fields = (
            '__all__'
        )


class DomainSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Domain
    """
    createTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    upTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Domain
        fields = (
            '__all__'
        )


