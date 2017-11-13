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

    # # 实现 create() 方法
    # def create(self, validated_data):
    #     return Agent(**validated_data)
    # #
    # # 实现 update() 方法
    # def update(self, instance, validated_data):
    #     instance.agtIP = validated_data.get('agtIP', instance.agtIP)
    #     instance.agtVersion = validated_data.get('agtVersion', instance.agtVersion)
    #     instance.agtStates = validated_data.get('agtStates', instance.agtStates)
    #     instance.remark = validated_data.get('remark', instance.remark)
    #     return instance

    class Meta:
        model = Agent
        fields = (
            '__all__'
        )

