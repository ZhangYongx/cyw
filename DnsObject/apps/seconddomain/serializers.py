# -*- coding: utf-8 -*-
from rest_framework import serializers
from seconddomain.models import SecondDomain


class SecondDomainSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = SecondDomain
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)


