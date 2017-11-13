# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Cname


class CnameSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Cname
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Cname
        fields = (
            '__all__'
        )

