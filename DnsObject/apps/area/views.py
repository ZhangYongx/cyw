# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from area import models
from area import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly


class AreaViewsSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer

    def create(self, request, *args, **kwargs):
        """
            添加信息，创建者和修改者默认为当前用户。IP转换为二进制存储
         """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
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
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_update(serializer)
        return Response(serializer.data)