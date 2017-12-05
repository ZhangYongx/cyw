# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user.username
        serializer.validated_data['update_user'] = self.request.user.username
        if serializer.validated_data['ip_choice'] == 0:
            serializer.validated_data['old_ip'] = IP(serializer.validated_data['old_ip']).strBin()
            serializer.validated_data['start_ip'] = ""
            serializer.validated_data['end_ip'] = ""
        elif serializer.validated_data['ip_choice'] == 1:
            serializer.validated_data['old_ip'] = ""
            serializer.validated_data['start_ip'] = IP(serializer.validated_data['start_ip']).strBin()
            serializer.validated_data['end_ip'] = IP(serializer.validated_data['end_ip']).strBin()
        serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
        self.perform_create(serializer)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """
            根据Id获取域名解析相关信息，并将二进制IP转换为点分十进制
        """
        instance = self.get_object()
        if instance.old_ip:
            instance.old_ip = ip_bin2int(instance.old_ip)
        if instance.start_ip:
            instance.start_ip = ip_bin2int(instance.start_ip)
        if instance.end_ip:
            instance.end_ip = ip_bin2int(instance.end_ip)
        instance.new_ip = ip_bin2int(instance.new_ip)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial )
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['update_user'] = self.request.user.username
        if serializer.validated_data['ip_choice'] == 0:
            serializer.validated_data['old_ip'] = IP(serializer.validated_data['old_ip']).strBin()
        elif serializer.validated_data['ip_choice'] == 1:
            serializer.validated_data['start_ip'] = IP(serializer.validated_data['start_ip']).strBin()
            serializer.validated_data['end_ip'] = IP(serializer.validated_data['end_ip']).strBin()
        serializer.validated_data['new_ip'] = IP(serializer.validated_data['new_ip']).strBin()
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Alias.objects.all()
        agt_id = self.request.query_params.get('agt_id', None)
        if agt_id:
            queryset = queryset.filter(agt_id=agt_id)
        for i in queryset:
            if i.old_ip:
                i.old_ip = ip_bin2int(i.old_ip)
            if i.start_ip:
                i.start_ip = ip_bin2int(i.start_ip)
            if i.end_ip:
                i.end_ip = ip_bin2int(i.end_ip)
            i.new_ip = ip_bin2int(i.new_ip)
        return queryset

