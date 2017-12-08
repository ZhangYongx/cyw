from rest_framework import serializers
from .models import Resolv
from PublicMethod.allserializers import AllSerializer


class ResolvSerializer(AllSerializer):
    """
        Serializer Models.Resolv
    """
    ip = serializers.IPAddressField(source='resolv_ip', read_only=True)

    class Meta:
        model = Resolv
        fields = (
            '__all__'
        )
        extra_kwargs = {'resolv_ip': {'write_only': True}}
