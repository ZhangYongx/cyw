# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import Host
from .serializers import HostSerializer


class HostViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 HostRecord API
    """
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        # serializer.validated_data['host_ip'] = IP(serializer.validated_data['host_ip']).strBin()
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        # serializer.validated_data['host_ip'] = IP(serializer.validated_data['host_ip']).strBin()
        self.perform_update(serializer)
        return Response(serializer.data)


