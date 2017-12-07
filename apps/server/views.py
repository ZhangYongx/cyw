# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PublicFunc.ip_int_bin import ip_bin2int
from rest_framework import status
# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import Server
from .serializers import ServerSerializer


class ServerViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Server API
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user.username
        serializer.validated_data['update_user'] = self.request.user.username
        serializer.validated_data['nameserver_ip'] = IP(serializer.validated_data['nameserver_ip']).strBin()
        self.perform_create(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.nameserver_ip = ip_bin2int(instance.nameserver_ip)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['update_user'] = self.request.user.username
        serializer.validated_data['nameserver_ip'] = IP(serializer.validated_data['nameserver_ip']).strBin()
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        """
        把 ipaddress 从二进制转换为十进制，之后传递给 serializer;
        可根据"区域id" 查询 ipaddress;
        """
        queryset = Server.objects.all()
        agt_id = self.request.query_params.get('agt_id', None)
        if agt_id:
            queryset = queryset.filter(agt_id=agt_id)
        for i in queryset:
            i.nameserver_ip = ip_bin2int(i.nameserver_ip)
        return queryset

