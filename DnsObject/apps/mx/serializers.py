# -*- coding: utf-8 -*-
from .models import Mx
from PublicMethod.allserializers import AllSerializer


class MxSerializer(AllSerializer):
    """
    序列化 Models.Mx
    """

    class Meta:
        model = Mx
        fields = '__all__'

