# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 16:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alias',
            name='ip_choice',
        ),
    ]
