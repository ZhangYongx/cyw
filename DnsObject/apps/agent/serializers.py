# -*- coding: utf-8 -*-
from rest_framework import serializers
from agent.models import Agent

class AgentSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Agent
    """
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Agent
        fields = (

            '__all__'
        )
        read_only_fields = ('create_user', 'update_user','token',)