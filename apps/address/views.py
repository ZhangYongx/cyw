# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from rest_framework import viewsets
from .models import Address
from .serializers import AddressSerializer

# Create your views here.


class AddressViewset(viewsets.ModelViewSet):
    """
    允许用户查看或编辑 Address API
    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
