# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from rest_framework import viewsets
from .models import SecondDomain
from .serializers import SecondDomainSerializer


class SecondDomainViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Domain API
    """
    queryset = SecondDomain.objects.all()
    serializer_class = SecondDomainSerializer

