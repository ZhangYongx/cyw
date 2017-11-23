# -*- coding: utf-8 -*-
# Author:zhangxun
from PublicFunc.serializers import AllSerializer
from .models import TopDomain


class TopDomainSerializer(AllSerializer):
    """
    Serializer Models.Domain
    """
    class Meta:
        model = TopDomain
        fields = '__all__'
        # read_only_field = ('create_user', 'update_user',)

