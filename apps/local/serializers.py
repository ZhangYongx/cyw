# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Local


class LocalSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Local
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Local
        fields = (
            '__all__'
        )

