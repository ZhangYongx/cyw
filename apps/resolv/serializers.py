# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import Resolv


class ResolvSerializer(AllSerializer):
    """
    Serializer Models.Resolv
    """
    class Meta:
        model = Resolv
        fields = '__all__'
        # read_only_field = ('create_user', 'update_user',)
