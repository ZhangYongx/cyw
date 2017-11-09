# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from users.models import DnsUserProfile


class Area(models.Model):
    """
        区域表
    """
    area_name = models.CharField(unique=True, max_length=45, verbose_name="区域简称")
    fullname = models.CharField(unique=True, max_length=45, verbose_name="区域")
    machine_room = models.CharField(unique=True, max_length=45, verbose_name="机房名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=45,  verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    responsible_name = models.ForeignKey(DnsUserProfile, models.DO_NOTHING, verbose_name="负责人",  db_column='responsible_name')

    class Meta:
        verbose_name = '区域'
        verbose_name_plural = verbose_name
        managed = True
        db_table = 'area'

    def __str__(self):
        return self.area_name