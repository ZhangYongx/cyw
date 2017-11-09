# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from IPy import IP
from rest_framework import viewsets
from rest_framework.response import Response
from PublicMethod.ipreplace import IpReplace
from address import models
from address import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly


class AddressViewsSet(viewsets.ModelViewSet):

    """
        list:
            域名解析相关信息
        retrieve:
            查询某条信息
        create:
            添加信息
        update:
            修改信息
        get_queryset：
            查询某个区域的相关信息
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    serializer_class = serializers.AddressSerializer

    def create(self, request, *args, **kwargs):
        """
            添加信息，创建者和修改者默认为当前用户。IP转换为二进制存储
         """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            serializer.validated_data['addr_ip'] = IP(serializer.validated_data['addr_ip']).strBin()
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
        serializer.validated_data['addr_ip'] = IP(serializer.validated_data['addr_ip']).strBin()
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_update(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
            根据Id获取域名解析相关信息，并将二进制IP转换为点分十进制
        """
        instance = self.get_object()
        instance.ip = IpReplace(instance.ip).bintoip()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):

        """
            根据区域id查询，获取相关数据，并将IP由二进制转换为点分十进制
        """
        queryset = models.Address.objects.all()
        areaid = self.request.query_params.get('areaid', None)
        if areaid is not None:
            queryset = queryset.filter(area_id=areaid)
        for i in queryset:
            i.ip = IpReplace(i.ip).bintoip()
        return queryset
