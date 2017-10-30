# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import time

# Create your models here.


class Area(models.Model):
    """
    区域表
    """
    areaname = models.CharField(db_column='areaName', max_length=45, blank=True, null=True)
    responsible = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        # managed = True
        db_table = 'area'


class Alias(models.Model):
    """
    Alias解析
    """
    aliasId = models.IntegerField()
    aliasForeign = models.ForeignKey('Area')
    oldip = models.GenericIPAddressField()
    startipEndip = models.CharField(max_length=200)
    newip = models.GenericIPAddressField()
    ipmask = models.GenericIPAddressField()
    remark = models.CharField(max_length=300, blank=True, null=True)
    createTime = models.DateField(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    upTime = models.DateField(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    updateUser = models.CharField(max_length=30,default="now user")

    class Meta:
        # managed = True
        db_table = 'alias'


class Cname(models.Model):
    """
    CName解析
    """
    cnameId = models.IntegerField()
    cnameForeign = models.ForeignKey('Area')
    cn = models.CharField(max_length=100)
    dns =  models.CharField(max_length=100)
    ttl = models.IntegerField(default=10)
    remark = models.CharField(max_length=300, blank=True, null=True)
    createTime = models.DateField(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    upTime = models.DateField(time.strftime('%Y-%m-%d', time.localtime(time.time())))
    updateUser = models.CharField(max_length=30, default='now user')

    class Meta:
        # managed = True
        db_table = 'cname'