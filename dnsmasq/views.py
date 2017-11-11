# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import re
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from django.db import models
from .models import *
from .serializers import *

# 检测域名格式
def validate_dnsname(data):
    reg = re.compile(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?', re.IGNORECASE)
    is_dnsname = reg.match(data)
    if is_dnsname:
        return True
    else:
        raise ValidationError(u'请输入正确的域名格式')

def validate_phone(num):
    reg = re.compile(r'(13\d|14[57]|15[^4,\D]|17[13678]|18\d)\d{8}|170[0589]\d{7}')
    is_phone = reg.match(num)
    if is_phone:
        return True
    else:
        raise ValidationError(u'请输入正确的手机格式')


class DNSUserViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 UserTable API
    """
    # createTime = models.DateTimeField(auto_created=True)
    queryset = DNSUser.objects.all()
    serializer_class = DNSUserSerializer


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


class IPinfoViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 IP API
    """
    queryset = IPinfo.objects.all()
    serializer_class = IPinfoSerializer


class TopDomainViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Domain API
    """
    queryset = TopDomain.objects.all()
    serializer_class = TopDomainSerializer


class SecondDomainViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Domain API
    """
    queryset = SecondDomain.objects.all()
    serializer_class = SecondDomainSerializer


class HostViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 HostRecord API
    """
    queryset = Host.objects.all()
    serializer_class = HostSerializer


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


class LoginfoViewset(viewsets.ModelViewSet):
    queryset = Loginfo.objects.all()
    serializer_class = LoginfoSerializer


class HeartbeatViewset(viewsets.ModelViewSet):
    queryset = Heartbeat.objects.all()
    serializer_class = HeartbeatSerializer