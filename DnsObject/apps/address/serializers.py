# -*- coding: utf-8 -*-
from rest_framework import serializers
from address import models
from PublicMethod.allserializers import AllSerializer


class AddressSerializer(AllSerializer):
    """
    序列化 Models.Address
    """
    ip = serializers.IPAddressField(source='addr_ip', read_only=True)

    class Meta:
        model = models.Address
        fields = (
            '__all__'
        )
        extra_kwargs = {'addr_ip': {'write_only': True}}