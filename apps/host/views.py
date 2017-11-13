# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Host
from .serializers import HostSerializer


class HostViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 HostRecord API
    """
    queryset = Host.objects.all()
    serializer_class = HostSerializer

