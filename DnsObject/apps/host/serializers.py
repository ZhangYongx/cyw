# -*- coding: utf-8 -*-
from .models import Host
from rest_framework import serializers
from PublicMethod.allserializers import AllSerializer


class HostSerializer(AllSerializer):
    """
    序列化 Models.HostRecord
    """
    ip = serializers.IPAddressField(source='host_ip', read_only=True)

    class Meta:
        model = Host
        fields = (
            '__all__'
        )
        extra_kwargs = {'host_ip': {'write_only': True}}
