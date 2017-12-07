# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PublicFunc.ip_int_bin import ip_bin2int
# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Server
from .serializers import ServerSerializer, ServerSerializer1, ServerSerializer2


class ServerViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Server API
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def get_serializer_class(self):
        """
        通过接受 URL 中 server_method 参数，来确定返回的序列化类型
        """
        if self.action == "create":
            if self.request.query_params.get('server_method') == '1':
                return ServerSerializer1
            elif self.request.query_params.get('server_method') == '2':
                return ServerSerializer2
            return ServerSerializer1
        return ServerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user.username
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_create(serializer)
        return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.nameserver_ip = ip_bin2int(instance.nameserver_ip)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        """
        可根据"agt_id" 查询序列化信息
        """
        queryset = Server.objects.all()
        agt_id = self.request.query_params.get('agt_id', None)
        if agt_id:
            queryset = queryset.filter(agt_id=agt_id)
        return queryset

