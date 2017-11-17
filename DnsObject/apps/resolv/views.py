# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Resolv
from .serializers import ResolvSerializer
from IPy import IP
from PublicMethod.ipreplace import IpReplace


class ResolvViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Resolv API
    """
    queryset = Resolv.objects.all()
    serializer_class = ResolvSerializer

    def create(self, request, *args, **kwargs):
        """
            添加信息，创建者和修改者默认为当前用户。IP转换为二进制存储
         """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            serializer.validated_data['resolv_ip'] = IP(serializer.validated_data['resolv_ip']).strBin()
            self.perform_create(serializer)
            return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
            根据Id获取域名解析相关信息，并将二进制IP转换为点分十进制
        """
        instance = self.get_object()
        instance.resolv_ip = IpReplace(instance.resolv_ip).bintoip()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        """
            根据区域id查询，获取相关数据，并将IP由二进制转换为点分十进制
        """
        queryset = Resolv.objects.all()
        agentid = self.request.query_params.get('agentid', None)
        if agentid is not None:
            queryset = queryset.filter(agentid=agentid)
        for i in queryset:
            i.resolv_ip = IpReplace(i.resolv_ip).bintoip()
        return queryset