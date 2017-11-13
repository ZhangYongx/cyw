# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Cname
from .serializers import CnameSerializer


class CnameViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Cname API
    """
    queryset = Cname.objects.all()
    serializer_class = CnameSerializer
