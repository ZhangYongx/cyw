# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Area


class AreaSerializer(AllSerializer):
    """
    序列化 Models.Area
    """
    class Meta:
        model = Area
        fields = '__all__'

