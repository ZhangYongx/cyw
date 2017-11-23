# -*- coding: utf-8 -*-
__author__ = "zhangxun"

from PublicFunc.serializers import AllSerializer
from .models import Address


class AddressSerializer(AllSerializer):
    """
    序列化 Models.Address
    """
    class Meta:
        model = Address
        fields = '__all__'

