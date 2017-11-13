# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Txt


class TxtSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Txt
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Txt
        fields = (
            '__all__'
        )
