# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import IPinfo
from .serializers import IPinfoSerializer


class IPinfoViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 IP API
    """
    queryset = IPinfo.objects.all()
    serializer_class = IPinfoSerializer

    def create(self, request, *args, **kwargs):
        """
        生成创建人信息
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        serializer.validated_data['ipaddress'] = IP(serializer.validated_data['ipaddress']).strBin()
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        生成更新人信息
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        serializer.validated_data['ipaddress'] = IP(serializer.validated_data['ipaddress']).strBin()
        return Response(serializer.data)
