# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import TopDomain


class TopDomainSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Domain
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = TopDomain
        fields = (
            '__all__'
        )
        read_only_field = ('create_user', 'delete_user',)

