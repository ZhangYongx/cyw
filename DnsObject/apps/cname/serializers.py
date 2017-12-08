# -*- coding: utf-8 -*-
from cname import models
from PublicMethod.allserializers import AllSerializer


class CnameSerializers(AllSerializer):
    """
    序列化 Models.Cname
    """

    class Meta:
        model = models.Cname
        fields = (
            '__all__'
        )
