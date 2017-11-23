# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from seconddomain.models import SecondDomain
from agent.models import Agent
from ipinfo.models import IPinfo


class Server(models.Model):
    """
    Server Table
    """
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名", blank=True, null=True)
    namereverse_ip = models.ForeignKey(IPinfo, to_field='reverse_ip',verbose_name="反向IP", blank=True, null=True,default=None)
    nameserver_ip = models.CharField(max_length=45, verbose_name="NS IP", help_text="请输入域名服务器的IP")
    nameserver_port = models.IntegerField(default=53, verbose_name="NS PORT", help_text="请输入域名服务器的端口")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    agentid = models.ForeignKey(Agent, to_field='agentid', verbose_name="Agent编号")

    class Meta:
        managed = True
        db_table = "server"
        unique_together = ('namereverse_ip', 'agentid')

    def __str__(self):
        return self.domain