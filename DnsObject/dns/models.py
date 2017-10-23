# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Area(models.Model):
    area = models.CharField(max_length=45, blank=True, null=True)
    responsible = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name = '区域'
        verbose_name_plural = verbose_name
        managed = False
        db_table = 'area'

    def __str__(self):
        return self.area

class Address(models.Model):
    domain = models.CharField(max_length=45, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域', related_name='areaid')

    class Meta:
        managed = False
        db_table = 'address'


class Agent(models.Model):
    agent_ip = models.CharField(max_length=32, blank=True, null=True)
    agent_version = models.CharField(max_length=45, blank=True, null=True)
    agent_statu = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey('Area', verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'agent'


class Alias(models.Model):
    old_ip = models.CharField(max_length=45, blank=True, null=True)
    start_ip = models.CharField(max_length=32, blank=True, null=True)
    end_ip = models.CharField(max_length=32, blank=True, null=True)
    new_ip = models.CharField(max_length=32, blank=True, null=True)
    mask = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey('Area', verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'alias'



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Cname(models.Model):
    target_domain = models.CharField(max_length=45, blank=True, null=True)
    domain = models.CharField(max_length=45, blank=True, null=True)
    ttl = models.IntegerField(blank=True, null=True)
    create_time = models.CharField(max_length=45, blank=True, null=True)
    update_time = models.CharField(max_length=45, blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cname'


class ComputerRoom(models.Model):
    computer_name = models.CharField(max_length=45, blank=True, null=True)
    responsible = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    ipinfo = models.ForeignKey('Ipinfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'computer_room'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doamin(models.Model):
    id = models.IntegerField(primary_key=True)
    sid = models.IntegerField(blank=True, null=True)
    multilevel = models.CharField(max_length=45, blank=True, null=True)
    full_domain = models.CharField(max_length=45, blank=True, null=True)
    analytic_type = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doamin'


class FDomain(models.Model):
    domain = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'f_domain'


class HostRecord(models.Model):
    domain = models.CharField(max_length=45, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    ttl = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'host-record'


class Ipinfo(models.Model):
    ip = models.IntegerField(blank=True, null=True)
    cname_id = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipinfo'


class Local(models.Model):
    local = models.CharField(max_length=45, blank=True, null=True)
    domain = models.CharField(max_length=45)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'local'


class Mx(models.Model):
    domain = models.CharField(max_length=45, blank=True, null=True)
    mail_domain = models.CharField(max_length=45, blank=True, null=True)
    preference = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'mx'


class Ptr(models.Model):
    ip = models.CharField(max_length=32, blank=True, null=True)
    domain = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'ptr'


class Resolv(models.Model):
    ip = models.IntegerField(blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'resolv'


class SDomain(models.Model):
    fid = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=45, blank=True, null=True)
    full_domain = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=30, blank=True, null=True)
    f_domain = models.ForeignKey(FDomain, models.DO_NOTHING)
    doamin = models.ForeignKey(Doamin, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 's_domain'


class Servere(models.Model):
    domain = models.CharField(max_length=45, blank=True, null=True)
    server_ptr = models.CharField(max_length=32, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'servere'


class Srv(models.Model):
    domain = models.CharField(max_length=45, blank=True, null=True)
    server_domain = models.CharField(max_length=45, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'srv'


class Txt(models.Model):
    domain = models.CharField(max_length=45, blank=True, null=True)
    mail_domain = models.CharField(max_length=45)
    preference = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = False
        db_table = 'txt'


class User(models.Model):
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    permission = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
