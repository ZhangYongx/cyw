# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from area.models import Area
# Create your models here.


class IPinfo(models.Model):
    """
    ip table
    """
    ipaddress = models.GenericIPAddressField(blank=False, null=False, unique=True, verbose_name="IP")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")

    class Meta:
        db_table = "ipinfo"

    def __str__(self):
        return self.ipaddress
