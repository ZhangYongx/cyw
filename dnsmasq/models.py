# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class Area(models.Model):
    """
    Area Table
    """
    areaname = models.CharField(db_column='areaName', max_length=45, blank=True, verbose_name="区域名")
    responsible = models.CharField(max_length=45, blank=True, verbose_name="负责人")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'area'

    def __str__(self):
        return self.areaname


class Alias(models.Model):
    """
    Alias Table
    """
    # aliasId = models.IntegerField()
    aliasForeign = models.ForeignKey('Area', verbose_name="Area外键")
    # 原始IP 与 IP段只能填写一个
    oldip = models.GenericIPAddressField(verbose_name="原IP")
    startipEndip = models.CharField(max_length=200, blank=True, verbose_name="IP段")
    newip = models.GenericIPAddressField(verbose_name="新IP", unique=True)
    ipmask = models.GenericIPAddressField(verbose_name="掩码")
    remark = models.CharField(max_length=300, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    updateUser = models.CharField(max_length=30, default='now user', verbose_name="更新用户")

    class Meta:
        # managed = True
        db_table = 'alias'


class Cname(models.Model):
    """
    Cname Table
    """
    # cnameId = models.IntegerField()
    cnameForeign = models.ForeignKey('Area', verbose_name="Area外键")
    #此处需检测域名的规范性
    cn = models.CharField(max_length=100, verbose_name="别名", unique=True)
    dns = models.CharField(max_length=100, verbose_name="原域名")
    ttl = models.IntegerField(default=10, verbose_name="TTL时间")
    remark = models.CharField(max_length=300, blank=True, null=True, verbose_name="备注")
    # 设置 editable= True的字段, 后台不会显示编辑
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    updateUser = models.CharField(max_length=30, default='now user', verbose_name="更新用户")

    class Meta:
        # managed = True
        db_table = 'cname'