# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Ptr
from .serializers import PtrSerializer


class PtrViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Ptr API
    """
    queryset = Ptr.objects.all()
    serializer_class = PtrSerializer

