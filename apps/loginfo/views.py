# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import Loginfo
from .serializers import LoginfoSerializer


class LoginfoViewset(viewsets.ModelViewSet):
    queryset = Loginfo.objects.all()
    serializer_class = LoginfoSerializer


