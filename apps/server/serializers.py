# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Server
from rest_framework import serializers


class ServerSerializer(AllSerializer):
    """
    序列化 Models.Server
    """
    reverseip = serializers.IPAddressField(source='reverse_ip', read_only=True)

    class Meta:
        model = Server
        fields = '__all__'
        extra_kwargs = {'reverse_ip': {"write_only": True}}

