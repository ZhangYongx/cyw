# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from agent.models import Agent

# Create your models here.


class Resolv(models.Model):
    """
    Resolv table
    """
    resolv_ip = models.GenericIPAddressField(verbose_name="IP")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    agt_id = models.ForeignKey(Agent, to_field='agt_id', verbose_name="Agent编号")

    class Meta:
        # managed = True
        db_table = 'resolv'
        unique_together = ('resolv_ip', 'agt_id')

    def __str__(self):
        return str(self.resolv_ip)
