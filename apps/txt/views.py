# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Txt
from .serializers import TxtSerializer


class TxtViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Txt API
    """
    queryset = Txt.objects.all()
    serializer_class = TxtSerializer

