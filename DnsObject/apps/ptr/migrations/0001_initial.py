# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0001_initial'),
        ('seconddomain', '__first__'),
        ('ipinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ptr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('create_user', models.CharField(default='now user', editable=False, max_length=30, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('update_user', models.CharField(default='now user', editable=False, max_length=30, verbose_name='\u66f4\u65b0\u7528\u6237')),
                ('remarks', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5907\u6ce8')),
                ('agentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Agent', to_field='agentid', verbose_name='Agent\u7f16\u53f7')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seconddomain.SecondDomain', to_field='domain', verbose_name='\u57df\u540d')),
                ('ptr_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipinfo.IPinfo', to_field='ipaddress', verbose_name='IP')),
            ],
            options={
                'db_table': 'ptr',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='ptr',
            unique_together=set([('domain', 'agentid')]),
        ),
    ]
