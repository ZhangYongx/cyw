# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from dnsuser.models import DNSUser

# Create your models here.


class Area(models.Model):
    """
    Area Table
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="区域简称", help_text="请填写区域的英文缩写")
    # sn = models.CharField(max_length=10, unique=True, verbose_name="sn")
    fullname = models.CharField(max_length=45, unique=True, blank=False, verbose_name="区域名")
    machine_name = models.CharField(max_length=45, unique=True, blank=False, null=False, verbose_name="机房名")
    responsible = models.ForeignKey(DNSUser, to_field='username', verbose_name="负责人")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'area'

    def __str__(self):
        return self.name

