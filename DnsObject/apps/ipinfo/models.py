# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from agent.models import Agent
from django.db import models
from PublicMethod.ipreplace import IpReplace

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
    agentid = models.ForeignKey(Agent, to_field='agentid', verbose_name="Agent编号")

    class Meta:
        managed = True
        db_table = "ipinfo"

    def __str__(self):
        return IpReplace(self.ipaddress).bintoip()