# -*- coding: utf-8 -*-
from area import models
from PublicMethod.allserializers import AllSerializer


class AreaSerializer(AllSerializer):

    class Meta:
        model = models.Area
        fields = (
            '__all__'
        )
