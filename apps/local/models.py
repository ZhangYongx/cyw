# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ipinfo.models import IPinfo
from agent.models import Agent

# Create your models here.


class Local(models.Model):
    """
    Local Table
    """
    domain = models.CharField(max_length=45, verbose_name="本地域名")
    ipaddress = models.ForeignKey(IPinfo, to_field='ipaddress', verbose_name="主机")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    agt_id = models.ForeignKey(Agent, to_field='agt_id', verbose_name="Agent编号")

    class Meta:
        db_table = "local"
        unique_together = ('ipaddress', 'agt_id')

    def __str__(self):
        return self.domain
