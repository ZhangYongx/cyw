# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Host
from rest_framework import serializers


class HostSerializer(AllSerializer):
    """
    序列化 Models.HostRecord
    """
    ipaddress = serializers.IPAddressField(source='host_ip', read_only=True)

    class Meta:
        model = Host
        fields = '__all__'
        extra_kwargs = {'host_ip': {'write_only': True}}
