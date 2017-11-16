# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import viewsets
from .models import Resolv
from .serializers import ResolvSerializer


class ResolvViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Resolv API
    """
    queryset = Resolv.objects.all()
    serializer_class = ResolvSerializer
