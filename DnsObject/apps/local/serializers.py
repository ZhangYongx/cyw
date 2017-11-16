# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Local


class LocalSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Local
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Local
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)
