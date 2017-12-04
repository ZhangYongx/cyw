# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import viewsets
from rest_framework.response import Response
from .models import Address
from .serializers import AddressSerializer

# Create your views here.


class AddressViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Address API
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        """
        生成创建人信息
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['create_user'] = self.request.user.username
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        生成更新人信息
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Address.objects.all()
        agt_id = self.request.query_params.get('agt_id', None)
        if agt_id is not None:
            queryset = queryset.filter(agt_id=agt_id)
        return queryset
