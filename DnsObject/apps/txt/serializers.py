# -*- coding: utf-8 -*-
from .models import Txt
from PublicMethod.allserializers import AllSerializer


class TxtSerializer(AllSerializer):
    """
    序列化 Models.Txt
    """

    class Meta:
        model = Txt
        fields = '__all__'
