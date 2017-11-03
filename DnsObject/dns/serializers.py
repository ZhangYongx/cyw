# -*- coding: utf-8 -*-
from rest_framework import serializers
from dns import models


class AliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alias
        fields = (
            "__all__"
        )


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Area
        fields = (
            '__all__'
        )


class AreaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = models.Area
        fields = (
            "__all__"
        )


class AddressSerializer(serializers.ModelSerializer):
    """
        域名解析信息
    """
    #外键关联
    area_id = serializers.StringRelatedField(source='area.id')
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.Address
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)


class CnameSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.Cname
        fields = (
            "__all__"
        )
        read_only_fields = ('create_user', 'update_user',)


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HostRecord
        fields = (
            "__all__"
        )


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Local
        fields = (
            "__all__"
        )


class MxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mx
        fields = (
            "__all__"
        )


class PtrSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ptr
        fields = (
            "__all__"
        )


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Servere
        fields = (
            "__all__"
        )


class SrvSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Srv
        fields = (
            "__all__"
        )


class TxtSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Txt
        fields = (
            "__all__"
        )


class AddressSerializer2(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = (
            "__all__"
        )


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.User
#         fields = (
#             "__all__"
#         )
