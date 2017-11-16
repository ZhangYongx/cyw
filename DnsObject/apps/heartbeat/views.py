# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from django.shortcuts import render
from heartbeat.models import Heartbeat
from serializers import HeartbeatSerializer
from rest_framework import mixins

class HeartBeatViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Heartbeat.objects.all()
    serializer_class = HeartbeatSerializer

