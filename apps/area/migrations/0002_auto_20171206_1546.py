# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='machine_room',
            field=models.CharField(max_length=45, verbose_name='\u673a\u623f\u540d'),
        ),
    ]
