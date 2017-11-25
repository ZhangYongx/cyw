# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from agent.models import Agent
from django.db import models

class Loginfo(models.Model):
    """
    日志表
    """
    log_state = (
        (0, '正常'),
        (1, '错误'),
        (2, 'unknown'),
    )
    time = models.IntegerField(verbose_name="时间戳")
    state = models.IntegerField(choices=log_state, default=0, verbose_name="状态")
    agentid = models.ForeignKey(Agent, to_field='agentid', verbose_name="Agent ID")
    message = models.CharField(max_length=100, blank=True, null=True, verbose_name="信息保留")

    class Meta:
        managed = True
        db_table = "loginfo"