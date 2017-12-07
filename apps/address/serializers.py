# -*- coding: utf-8 -*-
__author__ = "zhangxun"

from PublicFunc.serializers import AllSerializer
from rest_framework import serializers
from .models import Address


class AddressSerializer(AllSerializer):
    """
    序列化 Models.Address
    """
    # 在序列化层 对字段进行再操作，为 addr_ip 取一个别名
    ip = serializers.IPAddressField(source='addr_ip', read_only=True)

    class Meta:
        model = Address
        fields = ('addr_ip',
                  'ip',
                  'domain',
                  'create_time',
                  'update_time',
                  'create_user',
                  'update_user',
                  'agt_id',
                  'remarks',
                  )
        # extra_kwargs = {'addr_ip': {'write_only': True}}
