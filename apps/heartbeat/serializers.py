# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Heartbeat


class HeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartbeat
        fields = (
            '__all__'
        )
        read_only_field = ('create_user', 'update_user',)


