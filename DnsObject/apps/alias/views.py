# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import Alias
from .serializers import AliasSerializer
from rest_framework.response import Response
from IPy import IP
from PublicMethod.ipreplace import IpReplace

class AliasViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Alias API
    """
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer


    def create(self, request, *args, **kwargs):
        """
            添加信息，创建者和修改者默认为当前用户。IP转换为二进制存储
         """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            if serializer.validated_data['old_ip'] is not None:
                serializer.validated_data['old_ip'] = IP(serializer.validated_data['old_ip']).strBin()
            if serializer.validated_data['start_ip'] is not None:
                serializer.validated_data['start_ip']= IP(serializer.validated_data['start_ip']).strBin()
            if serializer.validated_data['end_ip'] is not None:
                serializer.validated_data['end_ip'] = IP(serializer.validated_data['end_ip']).strBin()
            serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
            self.perform_create(serializer)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
            修改信息，修改人默认为当前用户，如果IP有修改，将转换为二进制存储。
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_update(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
            根据Id获取域名解析相关信息，并将二进制IP转换为点分十进制
        """
        instance = self.get_object()
        if instance.old_ip is not  None:
            instance.old_ip = IpReplace(instance.old_ip).bintoip()
        if instance.start_ip is not None:
            instance.start_ip = IpReplace(instance.start_ip).bintoip()
        if instance.end_ip is not None:
            instance.end_ip = IpReplace(instance.end_ip).bintoip()
        instance.new_ip = IpReplace(instance.new_ip).bintoip()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):

        """
            根据区域id查询，获取相关数据，并将IP由二进制转换为点分十进制
        """
        queryset = Alias.objects.all()
        agentid = self.request.query_params.get('agentid', None)
        if agentid is not None:
            queryset = queryset.filter(agentid=agentid)
        for i in queryset:
            if i.old_ip is not None:
                i.old_ip = IpReplace(i.old_ip).bintoip()
            if i.start_ip is not None:
                i.start_ip = IpReplace(i.start_ip).bintoip()
            if i.end_ip is not None:
                i.end_ip = IpReplace(i.end_ip).bintoip()
            i.new_ip = IpReplace(i.new_ip).bintoip()
        return queryset
