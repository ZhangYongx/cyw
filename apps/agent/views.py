# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import Agent
from .serializers import AgentSerializer
from PublicFunc.ip_int_bin import ip_bin2int


class AgentViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Agent API
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def create(self, request, *args, **kwargs):
        """
        生成创建人信息
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user.username
        serializer.validated_data['update_user'] = self.request.user.username
        serializer.validated_data['agt_ip'] = IP(serializer.validated_data['agt_ip']).strBin()
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user.username
        serializer.validated_data['update_user'] = self.request.user.username
        serializer.validated_data['agt_ip'] = IP(serializer.validated_data['agt_ip']).strBin()
        self.perform_update(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        根据 ID 获取域名解析, 并将二进制 IP 转为十进制

        """
        instance = self.get_object()
        instance.agt_ip = ip_bin2int(instance.agt_ip)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Agent.objects.all()
        agt_id = self.request.query_params.get('agt_id', None)
        if agt_id is not None:
            queryset = queryset.filter(agt_id=agt_id)
        for i in queryset:
            i.agt_ip = ip_bin2int(i.agt_ip)
        return queryset
