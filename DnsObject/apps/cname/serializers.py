# -*- coding: utf-8 -*-
from rest_framework import serializers
from cname import models


class CnameSerializers(serializers.ModelSerializer):
    """
    序列化 Models.Cname
    """
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.Cname
        fields = (
            '__all__'
        )
        read_only_fields = ('create_user', 'update_user',)
