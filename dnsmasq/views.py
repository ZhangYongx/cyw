# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from django.db import models
from rest_framework import viewsets
from django.db import models
from .models import *
from .serializers import *


class UserTableViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 UserTable API
    """
    # createTime = models.DateTimeField(auto_created=True)
    queryset = UserTable.objects.all()
    serializer_class = UserTableSerializer


class AreaViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Area API
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class AgentViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Agent API
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class LocalViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Local API
    """
    queryset = Local.objects.all()
    serializer_class = LocalSerializer


class ServerViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Server API
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class AddressViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Address API
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class HostRecordViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 HostRecord API
    """
    queryset = HostRecord.objects.all()
    serializer_class = HostRecordSerializer


class PtrViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Ptr API
    """
    queryset = Ptr.objects.all()
    serializer_class = PtrSerializer


class SrvViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Srv API
    """
    queryset = Srv.objects.all()
    serializer_class = SrvSerializer


class MxViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Mx API
    """
    queryset = Mx.objects.all()
    serializer_class = MxSerializer


class TxtViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Txt API
    """
    queryset = Txt.objects.all()
    serializer_class = TxtSerializer


class CnameViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Cname API
    """
    queryset = Cname.objects.all()
    serializer_class = CnameSerializer


class AliasViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Alias API
    """
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer


class ResolvViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Resolv API
    """
    queryset = Resolv.objects.all()
    serializer_class = ResolvSerializer


class MachineRoomViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 MachineRoom API
    """
    queryset = MachineRoom.objects.all()
    serializer_class = MachineRoomSerializer


class IPViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 IP API
    """
    queryset = IP.objects.all()
    serializer_class = IPSerializer


class DomainViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Domain API
    """
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer