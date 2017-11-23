# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Server


class ServerSerializer(AllSerializer):
    """
    序列化 Models.Server
    """
    class Meta:
        model = Server
        fields = '__all__'
        # read_only_field = ('create_user', 'update_user',)


