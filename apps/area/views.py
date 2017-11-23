# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Area
from .serializers import AreaSerializer


class AreaViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Area API
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        # serializer.validated_data['sn'] = serializer.validated_data['fullname'] + serializer.validated_data['machine_name']
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial )
        serializer.is_valid()
        serializer.validated_data['create_user'] = self.request.user
        serializer.validated_data['update_user'] = self.request.user
        # serializer.validated_data['sn'] = serializer.validated_data['fullname'] + serializer.validated_data['machine_name']
        self.perform_update(serializer)
        return Response(serializer.data)

