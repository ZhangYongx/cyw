# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Local
from rest_framework import serializers


class LocalSerializer(AllSerializer):
    """
    序列化 Models.Local
    """
    ip = serializers.IPAddressField(source='ipaddress', read_only=True)

    class Meta:
        model = Local
        fields = '__all__'
        extra_kwargs = {'ipaddress': {'write_only': True}}
