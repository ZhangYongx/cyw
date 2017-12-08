# -*- coding: utf-8 -*-
from ipinfo.models import IPinfo
from PublicMethod.allserializers import AllSerializer


class IPinfoSerializer(AllSerializer):
    """
    Serializer Models.Ipinfo
    """

    class Meta:
        model = IPinfo
        fields = (
            '__all__'
        )
        read_only_fields = ('reverse_ip',)
