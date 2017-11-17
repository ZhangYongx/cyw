# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import Ptr
from .serializers import PtrSerializer
from rest_framework.response import Response


class PtrViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Ptr API
    """
    queryset = Ptr.objects.all()
    serializer_class = PtrSerializer

    def create(self, request, *args, **kwargs):
        """
            添加信息，创建者和修改者默认为当前用户。IP转换为二进制存储
         """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # serializer.validated_data['ptr_ip'] = IP(serializer.validated_data['ptr_ip']).strBin()
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_create(serializer)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
            修改信息，修改人默认为当前用户
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        # serializer.validated_data['ptr_ip'] = IP(serializer.validated_data['ptr_ip']).strBin()
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_update(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
            根据Id获取域名解析相关信息，并将二进制IP转换为点分十进制
        """
        instance = self.get_object()
        # instance.ptr_ip = IpReplace(instance.ptr_ip).bintoip()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):

        """
            根据区域id查询，获取相关数据
        """
        queryset = Ptr.objects.all()
        agentid = self.request.query_params.get('agentid', None)
        if agentid is not None:
            queryset = queryset.filter(agentid=agentid)
        # for i in queryset:
        #     i.ptr_ip = IpReplace(i.ptr_ip).bintoip()
        return queryset