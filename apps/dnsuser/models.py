# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class DNSUser(models.Model):
    """
    User Table
    """
    permission_choice = (
        (0, "普通用户"),
        (1, "管理员"),
        (2, "超级管理员"),
    )

    username = models.CharField(max_length=30, blank=False, null=False, unique=True, verbose_name="用户名")
    permission = models.IntegerField(choices=permission_choice, default=0, verbose_name="权限")
    email = models.EmailField(max_length=30, blank=False, null=False, unique=True, verbose_name="邮箱地址")
    qq = models.CharField(max_length=11, null=False, unique=True, verbose_name="QQ号")
    phone = models.CharField(max_length=11, null=False, unique=True, verbose_name="手机号")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    update_user = models.CharField(max_length=30, editable=False, verbose_name="更新用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        db_table = 'dnsuser'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

