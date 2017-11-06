# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from area.models import Area
from django.contrib.auth import get_user_model
User = get_user_model()


class Address(models.Model):
    """
        地址详细信息
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    ip = models.GenericIPAddressField(max_length=32, verbose_name="IP地址")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域', related_name='areaid')

    class Meta:
        managed = True
        db_table = 'address'

    def __str__(self):
        return self.domain
