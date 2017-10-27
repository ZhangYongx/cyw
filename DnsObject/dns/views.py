# -*- coding: utf-8 -*-
from __future__ import unicode_literals
<<<<<<< HEAD
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

=======
from dns import models
from dns import serializers
from rest_framework import viewsets
from dns import permissions
from rest_framework import mixins
from rest_framework.response import Response
from dns.ipreplace import IpReplace


class AddressViewsSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                      mixins.DestroyModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Address.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return serializers.AddressSerializer
        elif self.action == "create":
            return serializers.AddressSerializerDetail
        elif self.action == "update":
            return serializers.AddressSerializerDetail
        elif self.action == "partial_update":
            return serializers.AddressSerializerDetail
        # elif self.action == "list":
        #     return serializers.AddressSerializerDetail
        return serializers.AddressSerializerDetail

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.ip = IP(serializer.ip).strBin()
    #     serializer.is_valid(raise_exception=True)
    #     user = self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     instance.ip = IP(instance.ip).strBin()
    #     instance.save()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #
    #     if getattr(instance, '_prefetched_objects_cache', None):
    #         # If 'prefetch_related' has been applied to a queryset, we need to
    #         # forcibly invalidate the prefetch cache on the instance.
    #         instance._prefetched_objects_cache = {}
    #
    #     return Response(serializer.data)
    #
    # def perform_update(self, serializer):
    #     serializer.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.ip = IpReplace(instance.ip).bintoip()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # def list(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.ip = IpReplace(instance.ip).bintoip()
    #     serializer = self.get_serializer(instance)
    #     queryset = self.filter_queryset(serializer)
    #
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

class AliasViewSet(viewsets.ModelViewSet):
    queryset = models.Alias.objects.all()
    serializer_class = serializers.AliasSerializer
<<<<<<< HEAD
    permission_classes = (permissions.IsOwnerOrReadOnly,)
=======
    # permission_classes = (permissions.IsOwnerOrReadOnly,)
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6


class AreaViewsSetDetail(viewsets.ModelViewSet):
    queryset = models.Area.objects.all()
<<<<<<< HEAD
    serializer_class = serializers.AreaSerializer
=======
    serializer_class = serializers.AreaSerializer


class CnameViewsSet(viewsets.ModelViewSet):
    queryset = models.Cname.objects.all()
    serializer_class = serializers.CnameSerializer


class HostViewsSet(viewsets.ModelViewSet):
    queryset = models.HostRecord.objects.all()
    serializer_class = serializers.HostSerializer


class LostViewsSet(viewsets.ModelViewSet):
    queryset = models.Local.objects.all()
    serializer_class = serializers.LocalSerializer


class MxViewsSet(viewsets.ModelViewSet):
    queryset = models.Mx.objects.all()
    serializer_class = serializers.MxSerializer


class PtrViewsSet(viewsets.ModelViewSet):
    queryset = models.Ptr.objects.all()
    serializer_class = serializers.PtrSerializer


class ServerViewsSet(viewsets.ModelViewSet):
    queryset = models.Servere.objects.all()
    serializer_class = serializers.ServerSerializer


class SrvViewsSet(viewsets.ModelViewSet):
    queryset = models.Srv.objects.all()
    serializer_class = serializers.SrvSerializer


class TxtViewsSet(viewsets.ModelViewSet):
    queryset = models.Txt.objects.all()
    serializer_class = serializers.TxtSerializer

>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
