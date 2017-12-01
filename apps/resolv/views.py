# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from PublicFunc.ip_int_bin import ip_bin2int
# Create your views here.

import os
import sys

path = 'D:\\pyProject\\cidszx\\cidszx'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cidszx.settings")

from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import Resolv
from .serializers import ResolvSerializer


class ResolvViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Resolv API
    """
    queryset = Resolv.objects.all()
    serializer_class = ResolvSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            serializer.validated_data['resolv_ip'] = IP(serializer.validated_data['resolv_ip']).strBin()
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
        根据 ID 获取域名解析, 并将二进制 IP 转为十进制

        """
        instance = self.get_object()
        instance.resolv_ip = ip_bin2int(instance.resolv_ip)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.validated_data['update_user'] = self.request.user.username
            serializer.validated_data['resolv_ip'] = IP(serializer.validated_data['resolv_ip']).strBin()
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Resolv.objects.all()
        agt_id = self.request.query_params.get('agt_id', None)
        if agt_id:
            queryset = queryset.filter(agt_id=agt_id)
        for i in queryset:
            i.resolv_ip = ip_bin2int(i.resolv_ip)
        return queryset



