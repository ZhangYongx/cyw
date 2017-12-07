# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from .models import DNSUser
from .serializers import DNSUserSerializer


class DNSUserViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 UserTable API
    """
    queryset = DNSUser.objects.all()
    serializer_class = DNSUserSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['update_user'] = self.request.user.username
        self.perform_update(serializer)
        return Response(serializer.data)
