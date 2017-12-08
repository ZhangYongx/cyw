# -*- coding: utf-8 -*-
from agent.models import Agent
from PublicMethod.allserializers import AllSerializer


class AgentSerializer(AllSerializer):
    """
    序列化 Models.Agent
    """

    class Meta:
        model = Agent
        fields = '__all__'
        read_only_fields = ('token',)
