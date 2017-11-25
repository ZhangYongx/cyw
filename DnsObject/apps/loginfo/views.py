# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from .models import Loginfo
from .serializers import LoginfoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from utils.permissions import IsOwnerOrReadOnly

class LoginfoViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Loginfo.objects.all()
    serializer_class = LoginfoSerializer