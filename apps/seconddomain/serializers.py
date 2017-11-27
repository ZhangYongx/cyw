# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import SecondDomain


class SecondDomainSerializer(AllSerializer):
    """
    序列化 Models.Domain
    """
    class Meta:
        model = SecondDomain
        fields = '__all__'

