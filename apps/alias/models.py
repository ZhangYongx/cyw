# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from area import Area

# Create your models here.


class Alias(models.Model):
    """
    Alias Table
    """
    old_ip = models.GenericIPAddressField(default='169.254.7.1', blank=True, null=True, verbose_name="原IP")
    start_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="起始IP")
    end_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="结束IP")
    new_ip = models.GenericIPAddressField(verbose_name="新IP")
    ipmask = models.GenericIPAddressField(verbose_name="掩码")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'alias'
        unique_together = ('new_ip', 'area_name')

