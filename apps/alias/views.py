# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from IPy import IP
from .models import Alias
from .serializers import AliasSerializer
from PublicFunc.ip_int_bin import ip_bin2int


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
        if serializer.is_valid():
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            # serializer.validated_data['old_ip'] = IP(serializer.validated_data['old_ip']).strBin()
            # serializer.validated_data['start_ip'] = IP(serializer.validated_data['start_ip']).strBin()
            # serializer.validated_data['end_ip'] = IP(serializer.validated_data['end_ip']).strBin()
            # serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial )
        if serializer.is_valid():
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            # serializer.validated_data['old_ip'] = IP(serializer.validated_data['old_ip']).strBin()
            # serializer.validated_data['start_ip'] = IP(serializer.validated_data['start_ip']).strBin()
            # serializer.validated_data['end_ip'] = IP(serializer.validated_data['end_ip']).strBin()
            # serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Alias.objects.all()
        agt_id = self.request.query_params('agt_id', None)
        if agt_id:
            queryset = queryset.filter(agt_id=agt_id)
        for i in queryset:
            i.agt_ip = ip_bin2int(i.agt_ip)
        return queryset

