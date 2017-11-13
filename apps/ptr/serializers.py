# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Ptr


class PtrSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Ptr
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Ptr
        fields = (
            '__all__'
        )

