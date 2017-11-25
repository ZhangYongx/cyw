# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import Alias
from .serializers import AliasSerializer, AliasSerializer1, AliasSerializer2
from rest_framework.response import Response
from IPy import IP
from PublicMethod.ipreplace import IpReplace
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly
from rest_framework import status

class AliasViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Alias API
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer

    def get_serializer_class(self):
        if self.action =="create":
            if self.request.query_params.get('alias_method') =='1':
                return AliasSerializer1
            elif self.request.query_params.get('alias_method')=='2':
                return AliasSerializer2
            return AliasSerializer1
        return AliasSerializer

    def create(self, request, *args, **kwargs):
        """
            添加信息，创建者和修改者默认为当前用户。IP转换为二进制存储
         """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() and self.request.query_params.get('alias_method')=='1':
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            if serializer.validated_data['start_ip']:
                serializer.validated_data['start_ip']= IP(serializer.validated_data['start_ip']).strBin()
            if serializer.validated_data['end_ip']:
                serializer.validated_data['end_ip'] = IP(serializer.validated_data['end_ip']).strBin()
            serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif serializer.is_valid() and self.request.query_params.get('alias_method')=='2':
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            if serializer.validated_data['old_ip']:
                serializer.validated_data['old_ip'] = IP(serializer.validated_data['old_ip']).strBin()
            serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        """
            修改信息，修改人默认为当前用户，如果IP有修改，将转换为二进制存储。
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            if serializer.validated_data['old_ip']:
                serializer.validated_data['old_ip'] = IP(serializer.validated_data['old_ip']).strBin()
            if serializer.validated_data['start_ip']:
                serializer.validated_data['start_ip'] = IP(serializer.validated_data['start_ip']).strBin()
            if serializer.validated_data['end_ip']:
                serializer.validated_data['end_ip'] = IP(serializer.validated_data['end_ip']).strBin()
            serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
            根据Id获取域名解析相关信息，并将二进制IP转换为点分十进制
        """
        instance = self.get_object()
        if instance.old_ip:
            instance.old_ip = IpReplace(instance.old_ip).bintoip()
        if instance.start_ip:
            instance.start_ip = IpReplace(instance.start_ip).bintoip()
        if instance.end_ip:
            instance.end_ip = IpReplace(instance.end_ip).bintoip()
        instance.new_ip = IpReplace(instance.new_ip).bintoip()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):

        """
            根据agentid查询，获取相关数据，并将IP由二进制转换为点分十进制
        """
        queryset = Alias.objects.all()
        agentid = self.request.query_params.get('agentid', None)
        if agentid :
            queryset = queryset.filter(agentid=agentid)
        for i in queryset:
            if i.old_ip:
                i.old_ip = IpReplace(i.old_ip).bintoip()
            if i.start_ip:
                i.start_ip = IpReplace(i.start_ip).bintoip()
            if i.end_ip:
                i.end_ip = IpReplace(i.end_ip).bintoip()
            i.new_ip = IpReplace(i.new_ip).bintoip()
        return queryset
