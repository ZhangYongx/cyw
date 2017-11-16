# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Heartbeat(models.Model):
    """
    心跳表
    """
    heart_state = (
        (0, '正常'),
        (1, '告警'),
        (2, '错误'),
    )
    time = models.IntegerField(unique=True, verbose_name="时间戳")
    state = models.IntegerField(choices=heart_state, default=0, verbose_name="状态")
    agent_ip = models.GenericIPAddressField(verbose_name="Agent IP")
    message = models.CharField(max_length=10, blank=True, null=True, verbose_name="信息保留")

    class Meta:
        managed = True
        db_table = "Heartbeat"
