# -*- coding: utf-8 -*-
from __future__ import unicode_literals
<<<<<<< HEAD
from django.db import models


class Address(models.Model):
    """
    域名解析
    """
    domain_name = models.CharField(max_length=45, blank=True, null=True)
    ip = models.GenericIPAddressField(db_column='IP', blank=True, null=True)
    create_time = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    updateuser = models.CharField(max_length=45,null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey('Area', models.DO_NOTHING)
=======

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
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'address'


class Agent(models.Model):
<<<<<<< HEAD
    """
    Agent信息
    """
    areaid = models.IntegerField()
    agentip = models.IntegerField(db_column='agentIp', blank=True, null=True)
    agentversion = models.CharField(db_column='agentVersion', max_length=45, blank=True, null=True)
    agentstatu = models.CharField(db_column='agentStatu', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey('Area', models.DO_NOTHING)
=======
    agent_ip = models.CharField(max_length=32, blank=True, null=True)
    agent_version = models.CharField(max_length=45, blank=True, null=True)
    agent_statu = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey('Area', verbose_name='区域')
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'agent'


class Alias(models.Model):
<<<<<<< HEAD
    """
    Alias解析
    """
    areaid = models.IntegerField()
    oldip = models.CharField(db_column='oldIp', max_length=45, blank=True, null=True)
    startipendip = models.IntegerField(db_column='startIpEndIp', blank=True, null=True)
    newip = models.IntegerField(db_column='newIp', blank=True, null=True)
    mask = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    updateuser = models.CharField(db_column='updateUser', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey('Area', models.DO_NOTHING)
=======
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
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'alias'


<<<<<<< HEAD
class Area(models.Model):
    """
    区域表
    """
    areaname = models.CharField(db_column='areaName', max_length=45, blank=True, null=True)
    responsible = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class Cname(models.Model):
    """
    别名解析
    """
    areaid = models.IntegerField()
    cnamename = models.CharField(db_column='cnameName', max_length=45, blank=True, null=True)
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    ttl = models.IntegerField(db_column='TTL', blank=True, null=True)
=======

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
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
    create_time = models.CharField(max_length=45, blank=True, null=True)
    update_time = models.CharField(max_length=45, blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cname'


class ComputerRoom(models.Model):
<<<<<<< HEAD
    """
    机房信息表
    """
    computername = models.CharField(db_column='computerName', max_length=45, blank=True, null=True)
    responsible = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
=======
    computer_name = models.CharField(max_length=45, blank=True, null=True)
    responsible = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    ipinfo = models.ForeignKey('Ipinfo', models.DO_NOTHING)
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'computer_room'


<<<<<<< HEAD
class DoaminName(models.Model):
    """
    域名信息表
    """
    id = models.IntegerField(primary_key=True)
    sid = models.IntegerField(blank=True, null=True)
    multilevel = models.CharField(max_length=45, blank=True, null=True)
    fulldomainname = models.CharField(db_column='fullDomainName', max_length=45, blank=True, null=True)
    analytictype = models.CharField(db_column='analyticType', max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    createuser = models.CharField(db_column='createUser', max_length=30, blank=True, null=True)
=======
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
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
<<<<<<< HEAD
        db_table = 'doamin_name'


class FDomainName(models.Model):
    """
    顶级域名
    """
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    createuser = models.CharField(db_column='createUser', max_length=45, blank=True, null=True)
=======
        db_table = 'doamin'


class FDomain(models.Model):
    domain = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=45, blank=True, null=True)
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
<<<<<<< HEAD
        db_table = 'f_domain_name'


class HostRecord(models.Model):
    areaid = models.IntegerField()
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    ip = models.IntegerField(db_column='IP', blank=True, null=True)
    ttl = models.CharField(db_column='TTL', max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    updateuser = models.CharField(db_column='updateUser', max_length=30, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)
=======
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
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'host-record'


class Ipinfo(models.Model):
<<<<<<< HEAD
    """
    IP信息表
    """
    ip = models.IntegerField(blank=True, null=True)
    computerid = models.IntegerField(db_column='computerId', blank=True, null=True)
    remark = models.CharField(max_length=45, blank=True, null=True)
    computer_room = models.ForeignKey(ComputerRoom, models.DO_NOTHING, db_column='computer_Room_id')
=======
    ip = models.IntegerField(blank=True, null=True)
    cname_id = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=45, blank=True, null=True)
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'ipinfo'


class Local(models.Model):
<<<<<<< HEAD
    """
    本地解析
    """
    areaid = models.IntegerField()
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    updateuser = models.CharField(db_column='updateUser', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)
=======
    local = models.CharField(max_length=45, blank=True, null=True)
    domain = models.CharField(max_length=45)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'local'


class Mx(models.Model):
<<<<<<< HEAD
    """
    mx解析
    """
    areaid = models.IntegerField()
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    mailname = models.CharField(db_column='mailName', max_length=45, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    updateuser = models.CharField(db_column='updateUser', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)
=======
    domain = models.CharField(max_length=45, blank=True, null=True)
    mail_domain = models.CharField(max_length=45, blank=True, null=True)
    preference = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'mx'


class Ptr(models.Model):
<<<<<<< HEAD
    """
    ptr解析
    """
    areaid = models.IntegerField()
    ip = models.IntegerField(db_column='IP', blank=True, null=True)
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    updateuser = models.CharField(db_column='updateUser', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)
=======
    ip = models.CharField(max_length=32, blank=True, null=True)
    domain = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'ptr'


class Resolv(models.Model):
<<<<<<< HEAD
    """
    resolv解析
    """
    areaid = models.IntegerField()
    ip = models.IntegerField(db_column='IP', blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)
=======
    ip = models.IntegerField(blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'resolv'


<<<<<<< HEAD
class SDomainName(models.Model):
    """
    二级域名
    """
    fid = models.IntegerField(blank=True, null=True)
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    fulldomainname = models.CharField(db_column='fullDomainName', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    createuser = models.CharField(db_column='createUser', max_length=30, blank=True, null=True)
    f_domain_name = models.ForeignKey(FDomainName, models.DO_NOTHING)
    doamin_name = models.ForeignKey(DoaminName, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 's_domain_name'


class Servere(models.Model):
    """
    服务信息表
    """
    areaid = models.IntegerField()
    domain_name = models.CharField(max_length=45, blank=True, null=True)
    reverseip = models.IntegerField(db_column='reverseIp', blank=True, null=True)
    nsip = models.IntegerField(db_column='nsIp', blank=True, null=True)
    nsport = models.CharField(db_column='nsPort', max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    updateuser = models.CharField(db_column='updateUser', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)
=======
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
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'servere'


class Srv(models.Model):
<<<<<<< HEAD
    """
    srv解析
    """
    areaid = models.IntegerField()
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    serveraddr = models.CharField(db_column='serverAddr', max_length=45, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    priority = models.CharField(max_length=45, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    updateuser = models.CharField(db_column='updateUser', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)
=======
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
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'srv'


class Txt(models.Model):
<<<<<<< HEAD
    """
    txt解析
    """
    areaid = models.IntegerField()
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    text = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)
=======
    domain = models.CharField(max_length=45, blank=True, null=True)
    mail_domain = models.CharField(max_length=45)
    preference = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, verbose_name='区域')
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6

    class Meta:
        managed = False
        db_table = 'txt'


class User(models.Model):
<<<<<<< HEAD
    """
    用户信息表
    """
    username = models.CharField(db_column='userName', max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    permission = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
=======
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    permission = models.CharField(max_length=45, blank=True, null=True)
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
