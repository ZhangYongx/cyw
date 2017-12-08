# -*- coding: utf-8 -*-
from ptr.models import Ptr
from PublicMethod.allserializers import AllSerializer


class PtrSerializer(AllSerializer):
    """
    序列化 Models.Ptr
    """

    class Meta:
        model = Ptr
        fields = '__all__'
