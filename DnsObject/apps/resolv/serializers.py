from rest_framework import serializers
from .models import Resolv


class ResolvSerializer(serializers.ModelSerializer):
    """
        Serializer Models.Resolv
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    ip = serializers.IPAddressField(source='resolv_ip',read_only=True)
    class Meta:
        model = Resolv
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)
        extra_kwargs = {'resolv_ip': {'write_only': True}}