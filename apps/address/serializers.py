# -*- coding: utf-8 -*-
# Author:zhangxun

from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Address
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Address
        fields = (
            '__all__'
        )

