# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class SecondDomain(models.Model):
    domain = models.CharField(unique=True, max_length=45, verbose_name="域名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(max_length=30, verbose_name="创建者")
    update_user = models.CharField(max_length=30, verbose_name="修改者")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        verbose_name = '域名'
        verbose_name_plural = verbose_name
        managed = True
        db_table = 'second_domain'

    def __str__(self):
        return self.domain
