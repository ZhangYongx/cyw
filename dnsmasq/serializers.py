# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import *


class UserTableSerializer(serializers.ModelSerializer):
    """
    序列化 Models.UserTable
    """
    class Meta:
        model = UserTable
        fields = (
            '__all__'
        )


class AreaSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Area
    """
    class Meta:
        model = Area
        fields = (
            '__all__'
        )


class AgentSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Agent
    """

    class Meta:
        model = Agent
        fields = (
            '__all__'
        )


class LocalSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Local
    """
    class Meta:
        model = Local
        fields = (
            '__all__'
        )


class ServerSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Server
    """
    class Meta:
        model = Server
        fields = (
            '__all__'
        )


class AddressSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Address
    """
    class Meta:
        model = Address
        fields = (
            '__all__'
        )


class HostRecordSerializer(serializers.ModelSerializer):
    """
    序列化 Models.HostRecord
    """
    class Meta:
        model = HostRecord
        fields = (
            '__all__'
        )


class PtrSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Ptr
    """
    class Meta:
        model = Ptr
        fields = (
            '__all__'
        )


class SrvSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Srv
    """
    class Meta:
        model = Srv
        fields = (
            '__all__'
        )


class MxSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Mx
    """
    class Meta:
        model = Mx
        fields = (
            '__all__'
        )


class TxtSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Txt
    """
    class Meta:
        model = Txt
        fields = (
            '__all__'
        )


class CnameSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Cname
    """
    class Meta:
        model = Cname
        fields = (
            '__all__'
        )


class AliasSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Alias
    """
    class Meta:
        model = Alias
        fields = (
            '__all__'
        )


class ResolvSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Resolv
    """
    class Meta:
        model = Resolv
        fields = (
            '__all__'
        )


class MachineRoomSerializer(serializers.ModelSerializer):
    """
    Serializer Models.MachineRoom
    """
    class Meta:
        model = MachineRoom
        fields = (
            '__all__'
        )


class IPSerializer(serializers.ModelSerializer):
    """
    Serializer Models.IP
    """
    class Meta:
        model = IP
        fields = (
            '__all__'
        )


class DomainSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Domain
    """
    class Meta:
        model = Domain
        fields = (
            '__all__'
        )


