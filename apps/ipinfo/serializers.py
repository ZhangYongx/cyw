# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import IPinfo


class IPinfoSerializer(AllSerializer):
    """
    Serializer Models.IP
    """
    class Meta:
        model = IPinfo
        fields = '__all__'
