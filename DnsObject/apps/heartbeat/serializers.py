# -*- coding: utf-8 -*-
from rest_framework import serializers
from heartbeat.models import Heartbeat


class HeartbeatSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Heartbeat
    """
    class Meta:
        model = Heartbeat
        fields = (
            '__all__'
        )
        extra_kwargs = {'agent_ip': {'write_only': True}}