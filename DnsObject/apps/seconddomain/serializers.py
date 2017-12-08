# -*- coding: utf-8 -*-
from seconddomain.models import SecondDomain
from PublicMethod.allserializers import AllSerializer


class SecondDomainSerializer(AllSerializer):
    """
        Serializer Models.SecondDomain
     """

    class Meta:
        model = SecondDomain
        fields = '__all__'


