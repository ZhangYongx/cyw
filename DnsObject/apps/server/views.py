# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer, ServerSerializer1, ServerSerializer2
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly
from rest_framework import status


class ServerViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Server API
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

    def get_serializer_class(self):
        if self.action == "create":
            if self.request.query_params.get('server_method') == '1':
                return ServerSerializer1
            elif self.request.query_params.get('server_method') == '2':
                return ServerSerializer2
            return ServerSerializer1
        return ServerSerializer

    def create(self, request, *args, **kwargs):
        """
            添加信息，创建者和修改者默认为当前用户
         """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid() and self.request.query_params.get('server_method') =='1':
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif serializer.is_valid() and self.request.query_params.get('server_method') =='2':
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
            修改信息，修改人默认为当前用户
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):

        """
            根据agentid查询，获取相关数据
        """
        queryset = Server.objects.all()
        agentid = self.request.query_params.get('agentid', None)
        if agentid is not None:
            queryset = queryset.filter(agentid=agentid)
        return queryset
