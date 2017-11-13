# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Alias
from .serializers import AliasSerializer


class AliasViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Alias API
    """
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer

