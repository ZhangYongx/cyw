# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Alias


class AliasSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Alias
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Alias
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)