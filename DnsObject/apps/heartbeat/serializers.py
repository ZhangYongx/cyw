# -*- coding: utf-8 -*-
from heartbeat.models import Heartbeat
from PublicMethod.allserializers import AllSerializer


class HeartbeatSerializer(AllSerializer):
    """
    序列化 Heartbeat
    """
    class Meta:
        model = Heartbeat
        fields = (
            '__all__'
        )
