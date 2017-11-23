# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Alias


class AliasSerializer(AllSerializer):
    """
    序列化 Models.Alias
    """
    class Meta:
        model = Alias
        fields = '__all__'

