# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.

from rest_framework import viewsets
from .models import DNSUser
from .serializers import DNSUserSerializer


class DNSUserViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 UserTable API
    """
    # createTime = models.DateTimeField(auto_created=True)
    queryset = DNSUser.objects.all()
    serializer_class = DNSUserSerializer

