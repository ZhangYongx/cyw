# -*- coding: utf-8 -*-
# Author:zhangxun

from PublicFunc.serializers import AllSerializer
from .models import Ptr


class PtrSerializer(AllSerializer):
    """
    序列化 Models.Ptr
    """
    class Meta:
        model = Ptr
        fields = '__all__'

