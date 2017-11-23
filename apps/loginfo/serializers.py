# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Loginfo


class LoginfoSerializer(AllSerializer):
    """
    序列化 Loginfo表
    """
    class Meta:
        model = Loginfo
        fields = '__all__'
