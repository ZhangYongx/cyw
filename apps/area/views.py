# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Area
from .serializers import AreaSerializer


class AreaViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Area API
    """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

