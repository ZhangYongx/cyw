# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import Mx
from .serializers import MxSerializer


class MxViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Mx API
    """
    queryset = Mx.objects.all()
    serializer_class = MxSerializer
