# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from dns import models
from dns import serializers
from rest_framework import viewsets
from rest_framework.response import Response
from dns.ipreplace import IpReplace


class AddressViewsSet(viewsets.ModelViewSet):

    """
        list:
            域名解析相关信息
    """
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer

    def retrieve(self, request, *args, **kwargs):
        """
            根据IP获取域名解析相关信息，并将二进制数转换为点分十进制
        """
        instance = self.get_object()
        instance.ip = IpReplace(instance.ip).bintoip()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_queryset(self):

        """
            根据区域id查询，获取相关数据，并将IP由二进制转换为点分十进制
        """
        queryset = models.Address.objects.all()
        areaid = self.request.query_params.get('areaid', None)
        if areaid is not None:
            queryset = queryset.filter(area_id=areaid)
        for i in queryset:
            i.ip = IpReplace(i.ip).bintoip()
        return queryset


class AliasViewSet(viewsets.ModelViewSet):
    queryset = models.Alias.objects.all()
    serializer_class = serializers.AliasSerializer
    # permission_classes = (permissions.IsOwnerOrReadOnly,) 权限(非创建者仅有只读权限)


class AreaViewsSetDetail(viewsets.ModelViewSet):
    queryset = models.Area.objects.all()
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

