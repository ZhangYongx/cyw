# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import IPinfo
from .serializers import IPinfoSerializer


class IPinfoViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 IP API
    """
    queryset = IPinfo.objects.all()
    serializer_class = IPinfoSerializer

