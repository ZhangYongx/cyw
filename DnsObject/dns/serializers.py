# -*- coding: utf-8 -*-
from rest_framework import serializers
from dns import models
from IPy import IP
<<<<<<< HEAD
=======
from rest_framework.utils import model_meta
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6


class AliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alias
        fields = (
<<<<<<< HEAD
            'oldip',
            'startipendip',
            'newip',
=======
            'old_ip',
            'start_ip',
            'end_ip',
            'new_ip',
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
            'mask'
        )


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Area
        fields = (
            '__all__'
        )


<<<<<<< HEAD
=======
class AreaSerializer2(serializers.ModelSerializer):
    class Meta:
        model = models.Area
        fields = (
            'id',
        )


>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = (
<<<<<<< HEAD
            'domain_name',
=======
            'domain',
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
            'ip'
        )


<<<<<<< HEAD
"""
    域名解析详细信息
"""


class AddressSerializerDetail(serializers.ModelSerializer):
    #外键关联
    areaid = serializers.StringRelatedField(source='area.id')
=======
class AddressSerializerDetail(serializers.ModelSerializer):
    """
    list：
        域名解析信息
    """
    #外键关联
    area_id = serializers.StringRelatedField(source='area.id')

>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
    class Meta:
        model = models.Address
        fields = (
            '__all__'
        )

    def create(self, validated_data):
<<<<<<< HEAD
        address = super(AddressSerializerDetail,self).create(validated_data=validated_data)
=======
        # 将IP转化为二进制存储
        address = super(AddressSerializerDetail, self).create(validated_data=validated_data)
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
        address.ip = IP(address.ip).strBin()
        address.save()
        return address

<<<<<<< HEAD
=======
    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                field = getattr(instance, attr)
                field.set(value)
            else:
                setattr(instance, attr, value)
        instance.ip = IP(instance.ip).strBin()
        instance.save()
        return instance


class CnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cname
        fields = (
            "domain",
            "target_domain",
            "ttl"
        )


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HostRecord
        fields = (
            'domain',
            'ip',
            'ttl'
        )


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Local
        fields = (
            'domain',
        )


class MxSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mx
        fields = (
            'domain',
            'mail_domain',
            'preference'
        )


class PtrSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ptr
        fields = (
            'domain',
            'ip'
        )


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Servere
        fields = (
            'domain',
            'server_ptr',
            'ip',
            'port'
        )


class SrvSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Srv
        fields = (
            'domain',
            'server_domain',
            'port',
            'priority',
            'weight'
        )


class TxtSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Txt
        fields = (
            'domain',
            'mail_domain',
            'preference'
        )


class AddressSerializer2(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = (
            'domain',
            'ip'
        )


>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
