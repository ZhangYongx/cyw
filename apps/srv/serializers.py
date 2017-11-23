# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Srv


class SrvSerializer(AllSerializer):
    """
    序列化 Models.Srv
    """
    class Meta:
        model = Srv
        fields = '__all__'
        # read_only_field = ('create_user', 'update_user',)


