# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from django.db import models
from rest_framework import viewsets
from django.db import models
from .models import Area, Alias, Cname
from .serializers import AreaSerializer, AliasSerializer, CnameSerializer


# def index(request):
#     return HttpResponse("Welcome")


class AliasViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Alias API
    """
    # createTime = models.DateTimeField(auto_created=True)
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer


class CnameViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Cname API
    """
    queryset = Cname.objects.all()
    serializer_class = CnameSerializer


class AreaViewset(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer