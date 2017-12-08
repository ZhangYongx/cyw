# -*- coding: utf-8 -*-
from .models import TopDomain
from PublicMethod.allserializers import AllSerializer


class TopDomainSerializer(AllSerializer):
    """
    Serializer Models.TopDomain
    """

    class Meta:
        model = TopDomain
        fields = '__all__'
