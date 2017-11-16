# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Loginfo


class LoginfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loginfo
        fields = (
            '__all__'
        )
