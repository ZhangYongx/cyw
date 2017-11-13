# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Mx


class MxSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Mx
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Mx
        fields = (
            '__all__'
        )

