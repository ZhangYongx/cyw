# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Cname


class CnameSerializer(AllSerializer):
    """
    序列化 Models.Cname
    """
    class Meta:
        model = Cname
        fields = '__all__'


