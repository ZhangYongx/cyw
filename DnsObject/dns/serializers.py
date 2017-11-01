# -*- coding: utf-8 -*-
from rest_framework import serializers
from dns import models
from IPy import IP
from rest_framework.utils import model_meta
import time


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

    class Meta:
        model = models.Address
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        """
            存储数据时，将点分十进制IP转换为二进制存储
       """
        try:
            address = super(AddressSerializer, self).create(validated_data=validated_data)
            address.ip = IP(address.ip).strBin()
            # address.create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            address.save()
            return address
        except validated_data as e:
            print "数据格式错误"

    def update(self, instance, validated_data):
        """
            根据id更新信息
        """
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)
        instance.ip = IP(instance.ip).strBin()
        instance.update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        instance.save()
        return instance


class CnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cname
        fields = (
            "__all__"
        )


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


