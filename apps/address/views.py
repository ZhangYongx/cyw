# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import Address
from .serializers import AddressSerializer

# Create your views here.


class AddressViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Address API
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        """
        生成创建人信息
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        # serializer.validated_data['addr_ip'] = IP(serializer.validated_data['addr_ip']).strBin()
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        生成更新人信息
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        # serializer.validated_data['addr_ip'] = IP(serializer.validated_data['addr_ip']).strBin()
        self.perform_update(serializer)
        return Response(serializer.data)
