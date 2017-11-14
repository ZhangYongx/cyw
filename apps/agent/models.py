# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from area.models import Area

# Create your models here.


class Agent(models.Model):
    """
    Agent Table
    """
    live_states = (
        (0, "running"),
        (1, "down"),
        (2, "pause"),
        (3, "unknown"),
    )
    agt_ip = models.GenericIPAddressField(verbose_name="代理IP")
    agt_version = models.IntegerField(default=1, verbose_name="版本")
    agt_states = models.IntegerField(choices=live_states, default=1, verbose_name="运行状态")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")

    class Meta:
        db_table = 'agent'
        unique_together = ('agt_ip', 'area_name')

    def __str__(self):
        return str(self.agtIP)
