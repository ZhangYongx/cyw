# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Heartbeat


class HeartbeatSerializer(AllSerializer):
    """
    序列化 Heartbeat表
    """
    class Meta:
        model = Heartbeat
        fields = '__all__'


