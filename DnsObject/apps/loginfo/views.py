# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from .models import Loginfo
from .serializers import LoginfoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


class LoginfoViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Loginfo.objects.all()
    serializer_class = LoginfoSerializer

    def get_queryset(self):
        """
            根据agentid查询，获取相关数据
        """
        queryset = Loginfo.objects.all()
        agentid = self.request.query_params.get('agentid', None)
        if agentid is not None:
            queryset = queryset.filter(agentid=agentid)
        return queryset
