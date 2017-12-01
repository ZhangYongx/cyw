# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Mx
from .serializers import MxSerializer


class MxViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Mx API
    """
    queryset = Mx.objects.all()
    serializer_class = MxSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['create_user'] = self.request.user.username
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.validated_data['update_user'] = self.request.user.username
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



