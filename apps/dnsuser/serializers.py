# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import DNSUser


class DNSUserSerializer(serializers.ModelSerializer):
    """
    序列化 Models.UserTable
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = DNSUser
        fields = (
            '__all__'
        )
        read_only_field = ('update_user',)


