# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import SecondDomain


class SecondDomainSerializer(AllSerializer):
    """
    序列化 Models.Domain
    """
    class Meta:
        model = SecondDomain
        fields = '__all__'
        # read_only_field = ('create_user', 'update_user',)

