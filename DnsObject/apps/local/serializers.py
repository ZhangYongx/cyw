# -*- coding: utf-8 -*-

from .models import Local
from PublicMethod.allserializers import AllSerializer


class LocalSerializer(AllSerializer):
    """
    序列化 Models.Local
    """

    class Meta:
        model = Local
        fields = (
            '__all__'
        )
