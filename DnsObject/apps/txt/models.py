# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from agent.models import Agent
from seconddomain.models import SecondDomain


class Txt(models.Model):
    """
        TXT table
    """
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    text = models.TextField(max_length=45, verbose_name="TEXT")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    agentid = models.ForeignKey(Agent, to_field='agentid', verbose_name="Agent编号")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        db_table = 'txt'
        unique_together = ('domain', 'agentid')
        managed = True