# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Server
from .serializers import ServerSerializer


class ServerViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Server API
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer

