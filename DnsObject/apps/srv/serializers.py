# -*- coding: utf-8 -*-
from rest_framework import serializers
from srv.models import Srv


class SrvSerializer(serializers.ModelSerializer):
    """
    序列化 Models.Srv
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Srv
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)