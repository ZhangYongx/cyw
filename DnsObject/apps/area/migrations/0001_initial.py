# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 16:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=45, unique=True, verbose_name='\u533a\u57df\u7b80\u79f0')),
                ('fullname', models.CharField(max_length=45, unique=True, verbose_name='\u533a\u57df')),
                ('machine_room', models.CharField(max_length=45, unique=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('create_user', models.CharField(max_length=45, verbose_name='\u521b\u5efa\u8005')),
                ('update_user', models.CharField(max_length=45, verbose_name='\u4fee\u6539\u8005')),
                ('remarks', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5907\u6ce8')),
                ('responsible_name', models.ForeignKey(db_column='responsible_name', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='\u8d1f\u8d23\u4eba')),
            ],
            options={
                'verbose_name': '\u533a\u57df',
                'db_table': 'area',
                'managed': True,
                'verbose_name_plural': '\u533a\u57df',
            },
        ),
    ]
