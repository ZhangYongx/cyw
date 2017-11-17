# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import Txt
from .serializers import TxtSerializer
from rest_framework.response import Response

class TxtViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Txt API
    """
    queryset = Txt.objects.all()
    serializer_class = TxtSerializer

    def create(self, request, *args, **kwargs):
        """
            添加信息，创建者和修改者默认为当前用户
         """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():

            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_create(serializer)
            return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
            修改信息，修改人默认为当前用户
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
            根据区域查询，获取相关数据
        """
        queryset = Txt.objects.all()
        agentid = self.request.query_params.get('agentid', None)
        if agentid is not None:
            queryset = queryset.filter(agentid=agentid)
        return queryset