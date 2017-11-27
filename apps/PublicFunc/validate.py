# -*- coding: utf-8 -*-
__author__ = "zhangx"

import re
from django.core.exceptions import ValidationError


def validate_dnsname(data):
    """
    检测域名的正确格式
    :param data: domain
    :return: Bool
    """
    reg = re.compile(r'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?', re.IGNORECASE)
    match_dnsname = reg.match(data)
    if match_dnsname:
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
    match_phone = reg.match(num)
    if match_phone:
        return True
    else:
        raise ValidationError(u'请输入正确的手机格式')