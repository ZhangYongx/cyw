# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from agent.models import Agent
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
    time = models.IntegerField(verbose_name="时间戳")
    state = models.IntegerField(choices=heart_state, default=0, verbose_name="状态")
    agent_version = models.CharField(max_length=5, verbose_name="Agent版本" )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    agentid = models.ForeignKey(Agent, to_field='agentid', verbose_name="Agent ID")
    message = models.CharField(max_length=100, blank=True, null=True, verbose_name="信息保留")

    class Meta:
        managed = True
        db_table = "heartbeat"
