# -*- coding: utf-8 -*-
__author__ = "zhangx"

from rest_framework import serializers


class AllSerializer(serializers.ModelSerializer):
    """
    序列化模版
    """
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    # class Meta:
    #     # model = mn
    #     fields = '__all__'
