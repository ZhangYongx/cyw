# -*- coding: utf-8 -*-
from __future__ import unicode_literals
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

    class Meta:
        managed = False
        db_table = 'address'


class Agent(models.Model):
    """
    Agent信息
    """
    areaid = models.IntegerField()
    agentip = models.IntegerField(db_column='agentIp', blank=True, null=True)
    agentversion = models.CharField(db_column='agentVersion', max_length=45, blank=True, null=True)
    agentstatu = models.CharField(db_column='agentStatu', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey('Area', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'agent'


class Alias(models.Model):
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

    class Meta:
        managed = False
        db_table = 'alias'


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
    create_time = models.CharField(max_length=45, blank=True, null=True)
    update_time = models.CharField(max_length=45, blank=True, null=True)
    update_user = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cname'


class ComputerRoom(models.Model):
    """
    机房信息表
    """
    computername = models.CharField(db_column='computerName', max_length=45, blank=True, null=True)
    responsible = models.CharField(max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'computer_room'


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
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doamin_name'


class FDomainName(models.Model):
    """
    顶级域名
    """
    domainname = models.CharField(db_column='domainName', max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)
    createuser = models.CharField(db_column='createUser', max_length=45, blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
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

    class Meta:
        managed = False
        db_table = 'host-record'


class Ipinfo(models.Model):
    """
    IP信息表
    """
    ip = models.IntegerField(blank=True, null=True)
    computerid = models.IntegerField(db_column='computerId', blank=True, null=True)
    remark = models.CharField(max_length=45, blank=True, null=True)
    computer_room = models.ForeignKey(ComputerRoom, models.DO_NOTHING, db_column='computer_Room_id')

    class Meta:
        managed = False
        db_table = 'ipinfo'


class Local(models.Model):
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

    class Meta:
        managed = False
        db_table = 'local'


class Mx(models.Model):
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

    class Meta:
        managed = False
        db_table = 'mx'


class Ptr(models.Model):
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

    class Meta:
        managed = False
        db_table = 'ptr'


class Resolv(models.Model):
    """
    resolv解析
    """
    areaid = models.IntegerField()
    ip = models.IntegerField(db_column='IP', blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'resolv'


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

    class Meta:
        managed = False
        db_table = 'servere'


class Srv(models.Model):
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

    class Meta:
        managed = False
        db_table = 'srv'


class Txt(models.Model):
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

    class Meta:
        managed = False
        db_table = 'txt'


class User(models.Model):
    """
    用户信息表
    """
    username = models.CharField(db_column='userName', max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    permission = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime', blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
