# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 09:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0002_auto_20171110_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='createTime',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='createUser',
            new_name='create_user',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='upTime',
            new_name='update_time',
        ),
        migrations.RenameField(
            model_name='agent',
            old_name='updateUser',
            new_name='update_user',
        ),
    ]
