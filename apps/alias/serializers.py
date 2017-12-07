# -*- coding: utf-8 -*-
# Author:zhangxun

from rest_framework import serializers
from PublicFunc.serializers import AllSerializer
from .models import Alias


class AliasSerializer(AllSerializer):
    """
    序列化 Models.Alias
    """
    ip_choice = serializers.ChoiceField(choices=((0, '单个IP'), (1, 'IP地址段'),), default=0)

    def validate(self, data):
        """
        检验 old_ip 与 start_ip、end_ip，判断三者是否同时存在
        """
        if data['ip_choice'] == 0:
            # 用户选择 单ip, 则置空 ip段
            data['start_ip'] = ""
            data['end_ip'] = ""
        elif data['ip_choice'] == 1:
            # 选择 ip段, 则置空 原ip
            data['old_ip'] = ""
        else:
            raise serializers.ValidationError("「原IP」与「起始IP」、「结束IP」不能同时存在")
        return data

    class Meta:
        model = Alias
        fields = '__all__'

