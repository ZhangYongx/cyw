# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Alias, Cname, Area


class AliasSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Alias
    """
    class Meta:
        model = Alias
        fields = (
            '__all__'
        )


class CnameSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Cname
    """
    class Meta:
        model = Cname
        fields = (
            '__all__'
        )


class AreaSerializer(serializers.ModelSerializer):
    """
    Serializer Models.Area
    """
    class Meta:
        model = Area
        fields = (
            '__all__'
        )