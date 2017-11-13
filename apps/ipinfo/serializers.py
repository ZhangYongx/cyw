# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import IPinfo


class IPinfoSerializer(serializers.ModelSerializer):
    """
    Serializer Models.IP
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = IPinfo
        fields = (
            '__all__'
        )

