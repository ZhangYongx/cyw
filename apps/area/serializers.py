# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Area


class AreaSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Area
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Area
        fields = (
            '__all__'
        )
        read_only_field = ('create_user', 'update_user',)

