# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from seconddomain.models import SecondDomain
from agent.models import Agent

# Create your models here.


class Cname(models.Model):
    """
    Cname Table
    """
    cname = models.CharField(unique=True, max_length=100, verbose_name="别名")
    domain = models.ForeignKey(SecondDomain, to_field='domain',verbose_name="域名")
    ttl = models.IntegerField(default=10, verbose_name="TTL")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    agt_id = models.ForeignKey(Agent, to_field='agt_id', verbose_name="Agent编号")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'cname'
        verbose_name = '别名'
        verbose_name_plural = verbose_name
        unique_together = ('cname', 'agt_id', 'domain')

    def __str__(self):
        return self.cname

