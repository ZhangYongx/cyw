# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Local


class LocalSerializer(AllSerializer):
    """
    序列化 Models.Local
    """
    class Meta:
        model = Local
        fields = '__all__'
        # read_only_field = ('create_user', 'update_user',)
