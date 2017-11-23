# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import DNSUser


class DNSUserSerializer(AllSerializer):
    """
    序列化 Models.UserTable
    """
    class Meta:
        model = DNSUser
        fields = '__all__'


