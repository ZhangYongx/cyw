# -*- coding: utf-8 -*-
from rest_framework import serializers
from dns import models
from IPy import IP


class AliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alias
        fields = (
            'oldip',
            'startipendip',
            'newip',
            'mask'
        )


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Area
        fields = (
            '__all__'
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = (
            'domain_name',
            'ip'
        )


"""
    域名解析详细信息
"""


class AddressSerializerDetail(serializers.ModelSerializer):
    #外键关联
    areaid = serializers.StringRelatedField(source='area.id')
    class Meta:
        model = models.Address
        fields = (
            '__all__'
        )

    def create(self, validated_data):
        address = super(AddressSerializerDetail,self).create(validated_data=validated_data)
        address.ip = IP(address.ip).strBin()
        address.save()
        return address

