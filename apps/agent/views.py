# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import Agent
from .serializers import AgentSerializer


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
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        serializer.validated_data['agt_ip'] = IP(serializer.validated_data['agt_ip']).strBin()
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        serializer.validated_data['agt_ip'] = IP(serializer.validated_data['agt_ip']).strBin()
        self.perform_update(serializer)
        return Response(serializer.data)
