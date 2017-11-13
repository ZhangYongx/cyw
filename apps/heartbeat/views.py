# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Heartbeat
from .serializers import HeartbeatSerializer


class HeartbeatViewset(viewsets.ModelViewSet):
    queryset = Heartbeat.objects.all()
    serializer_class = HeartbeatSerializer
