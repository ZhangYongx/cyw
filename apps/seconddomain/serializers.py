# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import SecondDomain


class SecondDomainSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Domain
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = SecondDomain
        fields = (
            '__all__'
        )

