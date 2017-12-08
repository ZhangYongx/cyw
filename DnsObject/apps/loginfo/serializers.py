# -*- coding: utf-8 -*-
from .models import Loginfo
from PublicMethod.allserializers import AllSerializer


class LoginfoSerializer(AllSerializer):
    """
    序列化 Models.Loginfo
    """
    class Meta:
        model = Loginfo
        fields = '__all__'
