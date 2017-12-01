# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class AllViewset(viewsets.ModelViewSet):
    """
    为所有APP创建一个 Viewset模版, 获取当前用户名
    """

    def create(self, request, *args, **kwargs):
        """
        生成创建人信息
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['create_user'] = self.request.user.username
            # serializer.validated_data['update_user'] = self.request.user.username
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        """
        生成更新人信息
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            # serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

