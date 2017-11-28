# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Loginfo


class LoginfoSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Loginfo
    """
    class Meta:
        model = Loginfo
        fields = (
            '__all__'
        )
        extra_kwargs = {'agent_ip': {'write_only': True}}
