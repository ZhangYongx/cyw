# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from area.models import Area
from seconddomain.models import SecondDomain


class Cname(models.Model):
    cname = models.CharField(unique=True, max_length=45, verbose_name="别名")
    domain = models.ForeignKey(SecondDomain, models.DO_NOTHING, db_column='domain', verbose_name="二级域名")
    ttl = models.SmallIntegerField(default=600, verbose_name="生命周期")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=30, verbose_name="创建者")
    update_user = models.CharField(max_length=30, verbose_name="修改者")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', verbose_name="区域")

    class Meta:
        verbose_name = '别名'
        verbose_name_plural = verbose_name
        managed = True
        db_table = 'cname'

    def __str__(self):
        return self.cname
