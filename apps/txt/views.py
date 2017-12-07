# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from rest_framework import viewsets
# from django.contrib.auth import login
from rest_framework.response import Response
from .models import Txt
from .serializers import TxtSerializer


class TxtViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Txt API
    """
    queryset = Txt.objects.all()
    serializer_class = TxtSerializer

    def create(self, request, *args, **kwargs):
        """
        设置创建人、更新人默认为当前用户
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user.username
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        创建人保持不变，更新人为当前用户
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        """
        根据 agt_id 查询相关数据
        """
        queryset = Txt.objects.all()
        agt_id = self.request.query_params.get('agt_id', None)
        if agt_id:
            queryset = queryset.filter(agt_id=agt_id)
        return queryset
