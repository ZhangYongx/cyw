# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from seconddomain.models import SecondDomain
from ipinfo.models import IPinfo
from agent.models import Agent


class Host(models.Model):
    """
    主机记录
    """
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    host_ip = models.ForeignKey(IPinfo, to_field='ipaddress', verbose_name="IP地址")
    ttl = models.IntegerField(default=600, verbose_name="TTL")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    agentid = models.ForeignKey(Agent, to_field='agentid', verbose_name="Agent编号")

    class Meta:
        managed = True
        unique_together = ('host_ip', 'domain', 'agentid')
        db_table = 'host'


