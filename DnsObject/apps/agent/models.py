# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from PublicMethod.ipreplace import IpReplace


class Agent(models.Model):
    """
        Agent信息表
    """
    Agent_Status = (
        (0, '启动'),
        (1, '暂停'),
        (2, '停止'),
    )
    agt_ip = models.CharField(unique=True, max_length=39, verbose_name="Agent IP")
    agentid = models.CharField(unique=True, max_length=45, verbose_name="Agent编号")
    token = models.CharField(blank=True, null= True, max_length=100, verbose_name="Token")
    agt_version = models.CharField(max_length=5, verbose_name="版本")
    agt_state = models.IntegerField(choices=Agent_Status,verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    create_user = models.CharField(max_length=30,verbose_name="创建人")
    update_user = models.CharField(max_length=30,verbose_name="更新人")
    remarks = models.CharField(max_length=45, blank=True, null=True,verbose_name="备注")

    class Meta:
        managed = True
        db_table = 'agent'
        unique_together = ('agt_ip', 'agt_version', 'agentid')

    def __str__(self):
        return self.agentid


