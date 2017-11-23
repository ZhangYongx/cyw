# -*- coding: utf-8 -*-
# Author:zhangxun

from PublicFunc.serializers import AllSerializer
from .models import Mx


class MxSerializer(AllSerializer):
    """
    序列化 Models.Mx
    """
    class Meta:
        model = Mx
        fields = '__all__'
