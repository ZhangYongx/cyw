# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Loginfo(models.Model):
    """
    日志表
    """
    log_state = (
        (0, '正常'),
        (1, '错误'),
        (2, 'unknown'),
    )
    time = models.IntegerField(unique=True, verbose_name="时间戳")
    state = models.IntegerField(choices=log_state, default=0, verbose_name="状态")
    agent_ip = models.GenericIPAddressField(verbose_name="Agent IP")
    message = models.CharField(max_length=10, blank=True, null=True, verbose_name="信息保留")

    class Meta:
        db_table = "Loginfo"

