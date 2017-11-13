# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TopDomain(models.Model):
    """
    顶级域名
    """
    top_domain = models.CharField(max_length=45, unique=True, verbose_name="顶级域名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    delete_user = models.CharField(default='now user', editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        db_table = 'topdomain'

    def __str__(self):
        return self.top_domain
