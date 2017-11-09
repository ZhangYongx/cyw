# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class SecondDomain(models.Model):
    domain = models.CharField(unique=True, max_length=45)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name = '域名'
        verbose_name_plural = verbose_name
        managed = True
        db_table = 'second_domain'

    def __str__(self):
        return self.domain
