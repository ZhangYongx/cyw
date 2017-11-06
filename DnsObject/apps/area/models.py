# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Area(models.Model):
    """
        区域表
    """
    area = models.CharField(max_length=45, verbose_name="区域简称")
    area_name = models.CharField(max_length=45, verbose_name="区域")
    responsible = models.CharField(max_length=45, verbose_name="负责人")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=45,  verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = '区域'
        verbose_name_plural = verbose_name
        managed = True
        db_table = 'area'

    def __str__(self):
        return self.area