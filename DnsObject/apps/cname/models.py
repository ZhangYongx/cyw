# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from area.models import Area
from seconddomain.models import SecondDomain


class Cname(models.Model):
    cname = models.CharField(unique=True, max_length=45)
    domain = models.ForeignKey(SecondDomain, models.DO_NOTHING, db_column='domain')
    ttl = models.SmallIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name')

    class Meta:
        verbose_name = '别名'
        verbose_name_plural = verbose_name
        managed = True
        db_table = 'cname'

    def __str__(self):
        return self.cname
