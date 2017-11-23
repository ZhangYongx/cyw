# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Txt


class TxtSerializer(AllSerializer):
    """
    序列化 Models.Txt
    """
    class Meta:
        model = Txt
        fields = '__all__'
        # read_only_field = ('create_user', 'update_user',)
