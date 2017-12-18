# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Agent(models.Model):
    """
    Agent Table
    """
    live_states = (
        (0, "running"),
        (1, "down"),
        (2, "pause"),
    )
    agt_ip = models.GenericIPAddressField(unique=True, verbose_name="代理IP")
    agt_id = models.CharField(max_length=30, unique=True, verbose_name="Agent编号")
    agt_version = models.CharField(max_length=5, default='', verbose_name="版本")
    agt_states = models.IntegerField(choices=live_states, default=1, verbose_name="运行状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        db_table = 'agent'
        unique_together = ('agt_ip', 'agt_version', 'agt_id')

    def __str__(self):
        return str(self.agt_id)
