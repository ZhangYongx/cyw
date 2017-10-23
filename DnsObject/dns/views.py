# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from dns import models
from dns import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from dns import permissions


class AddressViewsSet(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer


class AddressViewsSetDetail(viewsets.ModelViewSet):
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializerDetail


class AliasViewSet(viewsets.ModelViewSet):
    queryset = models.Alias.objects.all()
    serializer_class = serializers.AliasSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)


class AreaViewsSetDetail(viewsets.ModelViewSet):
    queryset = models.Area.objects.all()
    serializer_class = serializers.AreaSerializer