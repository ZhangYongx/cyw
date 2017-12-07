# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import IPinfo
from .serializers import IPinfoSerializer
from PublicFunc.ip_int_bin import ip_bin2int


class IPinfoViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 IP API
    """
    queryset = IPinfo.objects.all()
    serializer_class = IPinfoSerializer

    def create(self, request, *args, **kwargs):
        """
        生成创建人信息
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user.username
        serializer.validated_data['update_user'] = self.request.user.username
        serializer.validated_data['reverse_ip'] = IP(serializer.validated_data['ipaddress']).reverseNames()[0]
        serializer.validated_data['ipaddress'] = IP(serializer.validated_data['ipaddress']).strBin()
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        生成更新人信息
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['update_user'] = self.request.user.username
        serializer.validated_data['reverse_ip'] = IP(serializer.validated_data['ipaddress']).reverseNames()[0]
        serializer.validated_data['ipaddress'] = IP(serializer.validated_data['ipaddress']).strBin()
        self.perform_update(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
        根据 ID 获取域名解析, 并将二进制 IP 转为十进制

        """
        instance = self.get_object()
        instance.ipaddress = ip_bin2int(instance.ipaddress)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):
        """
        把 ipaddress 从二进制转换为十进制，之后传递给 serializer;
        可根据"区域id" 查询 ipaddress;
        """
        queryset = IPinfo.objects.all()
        agt_id = self.request.query_params.get('agt_id', None)
        if agt_id:
            queryset = queryset.filter(agt_id=agt_id)
        for i in queryset:
            i.ipaddress = ip_bin2int(i.ipaddress)
        return queryset

