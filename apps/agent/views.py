# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import Agent
from .serializers import AgentSerializer


class AgentViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Agent API
    """
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

