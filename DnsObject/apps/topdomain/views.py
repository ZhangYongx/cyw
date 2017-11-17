# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import TopDomain
from .serializers import TopDomainSerializer
from rest_framework.response import Response

class TopDomainViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Domain API
    """
    queryset = TopDomain.objects.all()
    serializer_class = TopDomainSerializer

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

