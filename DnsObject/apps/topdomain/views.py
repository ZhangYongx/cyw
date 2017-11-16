# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import TopDomain
from .serializers import TopDomainSerializer


class TopDomainViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Domain API
    """
    queryset = TopDomain.objects.all()
    serializer_class = TopDomainSerializer

