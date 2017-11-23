# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Agent


class AgentSerializer(AllSerializer):
    """
    序列化 Models.Agent
    """
    class Meta:
        model = Agent
        fields = '__all__'


