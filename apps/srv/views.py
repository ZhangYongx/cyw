# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Srv
from .serializers import SrvSerializer


class SrvViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Srv API
    """
    queryset = Srv.objects.all()
    serializer_class = SrvSerializer

