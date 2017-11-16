# -*- coding: utf-8 -*-
# Author:zhangxun
from rest_framework import serializers
from .models import Loginfo


class LoginfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loginfo
        fields = (
            '__all__'
        )
