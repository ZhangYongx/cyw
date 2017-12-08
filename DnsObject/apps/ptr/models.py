# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from seconddomain.models import SecondDomain
from ipinfo.models import IPinfo
from agent.models import Agent


class Ptr(models.Model):
    """
    PTR table
    """
    ptr_ip = models.ForeignKey(IPinfo, to_field='reverse_ip', verbose_name="IP", blank=True, null=True)
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    agentid = models.ForeignKey(Agent, to_field='agentid', verbose_name="Agent编号")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        managed = True
        db_table = 'ptr'
        unique_together = ('domain', 'agentid')

