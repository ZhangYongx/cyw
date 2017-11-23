# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Host


class HostSerializer(AllSerializer):
    """
    序列化 Models.HostRecord
    """
    class Meta:
        model = Host
        fields = '__all__'
