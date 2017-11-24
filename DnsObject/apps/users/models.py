# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class DnsUserProfile(AbstractUser):
    """
        用户信息表
    """
    User_Permission = (
        (1, "普通用户"),
        (2, "管理员"),
        (3, "创建人"),
    )

    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    qq = models.CharField(max_length=11, blank=True, null=True, verbose_name="QQ")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    permission = models.IntegerField(choices=User_Permission, default=1, verbose_name="权限")
    update_user = models.CharField(max_length=30, verbose_name="修改者")
    remarks = models.CharField(max_length=100, null=True, blank=True, verbose_name="备注")

    class Meta:
        managed = True
        db_table = 'dnsuser'

    def __str__(self):
        return self.username