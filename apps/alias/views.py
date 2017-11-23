# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import Alias
from .serializers import AliasSerializer


class AliasViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Alias API
    """
    # 存放在 POST 方法
    # if Alias.ip_choice == 0:
    #     queryset = Alias.objects.defer('start_ip', 'end_ip')
    # else:
    #     queryset = Alias.objects.defer('old_ip')
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        # serializer.validated_data['old_ip'] = IP(serializer.validated_data['old_ip']).strBin()
        # serializer.validated_data['start_ip'] = IP(serializer.validated_data['start_ip']).strBin()
        # serializer.validated_data['end_ip'] = IP(serializer.validated_data['end_ip']).strBin()
        # serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial )
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        # serializer.validated_data['old_ip'] = IP(serializer.validated_data['old_ip']).strBin()
        # serializer.validated_data['start_ip'] = IP(serializer.validated_data['start_ip']).strBin()
        # serializer.validated_data['end_ip'] = IP(serializer.validated_data['end_ip']).strBin()
        # serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
        self.perform_update(serializer)
        return Response(serializer.data)

