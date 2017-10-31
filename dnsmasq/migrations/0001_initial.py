# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldip', models.GenericIPAddressField(verbose_name='\u539fIP')),
                ('startipEndip', models.CharField(blank=True, max_length=200, verbose_name='IP\u6bb5')),
                ('newip', models.GenericIPAddressField(verbose_name='\u65b0IP')),
                ('ipmask', models.GenericIPAddressField(verbose_name='\u63a9\u7801')),
                ('remark', models.CharField(blank=True, max_length=300, null=True, verbose_name='\u5907\u6ce8')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('upTime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updateUser', models.CharField(default='now user', max_length=30, verbose_name='\u66f4\u65b0\u7528\u6237')),
            ],
            options={
                'db_table': 'alias',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaname', models.CharField(blank=True, db_column='areaName', max_length=45, verbose_name='\u533a\u57df\u540d')),
                ('responsible', models.CharField(blank=True, max_length=45, verbose_name='\u8d1f\u8d23\u4eba')),
                ('remarks', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='Cname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cn', models.CharField(max_length=100, verbose_name='\u522b\u540d')),
                ('dns', models.CharField(max_length=100, verbose_name='\u539f\u57df\u540d')),
                ('ttl', models.IntegerField(default=10, verbose_name='TTL\u65f6\u95f4')),
                ('remark', models.CharField(blank=True, max_length=300, null=True, verbose_name='\u5907\u6ce8')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('upTime', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('updateUser', models.CharField(default='now user', max_length=30, verbose_name='\u66f4\u65b0\u7528\u6237')),
                ('cnameForeign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnsmasq.Area', verbose_name='Area\u5916\u952e')),
            ],
            options={
                'db_table': 'cname',
            },
        ),
        migrations.AddField(
            model_name='alias',
            name='aliasForeign',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnsmasq.Area', verbose_name='Area\u5916\u952e'),
        ),
    ]
