# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from area.models import Agent

# Create your models here.


class SecondDomain(models.Model):
    """
    次级域名
    """
    domain = models.CharField(max_length=45, unique=True, verbose_name="次级域名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    agt_id = models.ForeignKey(Agent, to_field='agt_id', verbose_name="Agent 编号")

    class Meta:
        db_table = "second_domain"

    def __str__(self):
        return self.domain

