# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from agent.models import Agent
from PublicFunc.ip_int_bin import ip_bin2int
# Create your models here.


class IPinfo(models.Model):
    """
    ip table
    """
    ipaddress = models.GenericIPAddressField(blank=False, null=False, unique=True, verbose_name="IP")
    reverse_ip = models.CharField(max_length=39, unique=True, editable=False, verbose_name="反向IP")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    agt_id = models.ForeignKey(Agent, to_field='agt_id', verbose_name="Agent编号")

    class Meta:
        db_table = "ipinfo"

    def __str__(self):
        return ip_bin2int(self.ipaddress)
