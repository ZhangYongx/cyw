# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import re
from django.core.exceptions import ValidationError

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


def validate_dnsname(data):
    """
    检测域名的正确格式
    :param data: domain
    :return: Bool
    """
    reg = re.compile(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?', re.IGNORECASE)
    is_dnsname = reg.match(data)
    if is_dnsname:
        return True
    else:
        raise ValidationError(u'请输入正确的域名格式')


def validate_phone(num):
    """
    检测手机的正确格式
    :param num: phone_num
    :return: Bool
    """
    reg = re.compile(r'(13\d|14[57]|15[^4,\D]|17[13678]|18\d)\d{8}|170[0589]\d{7}')
    is_phone = reg.match(num)
    if is_phone:
        return True
    else:
        raise ValidationError(u'请输入正确的手机格式')