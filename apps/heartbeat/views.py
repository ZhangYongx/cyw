# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import viewsets
from .models import Heartbeat
from .serializers import HeartbeatSerializer


class HeartbeatViewset(viewsets.ModelViewSet):
    queryset = Heartbeat.objects.all()
    serializer_class = HeartbeatSerializer

    def get_queryset(self):
        queryset = Heartbeat.objects.all()
        agt_id = self.request.query_params.get('agt_id', None)
        if agt_id is not None:
            queryset = queryset.filter(agt_id=agt_id)
        return queryset

