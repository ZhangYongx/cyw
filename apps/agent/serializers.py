# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Agent


class AgentSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Agent
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Agent
        fields = (
            '__all__'
        )
        read_only_field = ('create_user', 'update_user',)

