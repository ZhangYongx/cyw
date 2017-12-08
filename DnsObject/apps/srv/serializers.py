# -*- coding: utf-8 -*-
from srv.models import Srv
from PublicMethod.allserializers import AllSerializer


class SrvSerializer(AllSerializer):
    """
    序列化 Models.Srv
    """

    class Meta:
        model = Srv
        fields = '__all__'
