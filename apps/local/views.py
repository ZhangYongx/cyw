# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Local
from .serializers import LocalSerializer


class LocalViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Local API
    """
    queryset = Local.objects.all()
    serializer_class = LocalSerializer

