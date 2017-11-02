# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.


class ComOjbect(models.Model):
    """
    各表常用字段
    """
    currentime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    uptime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    currentuser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    upuser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")


class UserTable(models.Model):
    """
    User Table
    """
    username = models.CharField(blank=False, null=False, max_length=30, verbose_name="用户名")
    userAccount = models.CharField(blank=False, null=False, max_length=30, verbose_name="账户")
    userPasswd = models.CharField(blank=False, null=False, max_length=30, verbose_name="密码")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        db_table = 'usertable'

    def __str__(self):
        return self.username


class Area(models.Model):
    """
    Area Table
    """
    name = models.CharField(max_length=10, verbose_name="区域简称")
    fullname = models.CharField(max_length=45, blank=False, verbose_name="区域名")
    responsible = models.CharField(max_length=45, blank=True, verbose_name="负责人")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")

    class Meta:
        # managed = True
        db_table = 'area'

    def __str__(self):
        return self.name


class Agent(models.Model):
    """
    Agent Table
    """
    liveStates = (('r', "running"),
                  ('d', "down"),
                  ('p', "pause"),
                  ('u', "unknown"),
                  )
    agtIP = models.GenericIPAddressField(verbose_name="代理IP")
    agtVersion = models.IntegerField(verbose_name="版本")
    agtStates = models.IntegerField(choices=liveStates, verbose_name="运行状态")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        db_table = 'agent'

    def __str__(self):
        return str(self.agtIP)


class Local(models.Model):
    """
    Local Table
    """
    domain = models.CharField(max_length=45, verbose_name="本地域名")
    localIP = models.GenericIPAddressField(verbose_name="本地IP")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        db_table = "local"

    def __str__(self):
        return self.domain


class Server(models.Model):
    """
    Server Table
    """
    domain = models.CharField(max_length=45, unique=True, verbose_name="域名")
    serverIP = models.GenericIPAddressField(verbose_name="反向")
    nameServerIP = models.GenericIPAddressField(verbose_name="域名服务器IP")
    nameServerPort = models.IntegerField(default=53, verbose_name="域名服务器端口")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        db_table = "server"

    def __str__(self):
        return self.domain


class Address(models.Model):
    """
    Address Table
    """
    addressIP = models.GenericIPAddressField(verbose_name="IP地址")
    domain = models.CharField(max_length=45, verbose_name="域名")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'address'

    def __str__(self):
        return str(self.addressIP)


class HostRecord(models.Model):
    """
    主机记录
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    hostIP = models.GenericIPAddressField(verbose_name="IP地址")
    ttl = models.IntegerField(default=10, verbose_name="TTL")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'hostrecord'

    def __str__(self):
        return self.domain


class Ptr(models.Model):
    """
    PTR table
    """
    ptrIP = models.GenericIPAddressField(verbose_name="IP")
    domain = models.CharField(max_length=45, verbose_name="域名")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'ptr'

    def __str__(self):
        return str(self.ptrIP)


class Srv(models.Model):
    """
    SRV Table
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    serviceDomain = models.CharField(max_length=45, verbose_name="服务地址")
    srvPort = models.IntegerField(default='', verbose_name="端口")
    priority = models.IntegerField( verbose_name="优先级")
    weight = models.IntegerField(default=10, verbose_name="权重")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'srv'

    def __str__(self):
        return self.domain


class Mx(models.Model):
    """
    mail server table
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    mxDomain = models.CharField(max_length=45, verbose_name="服务地址")
    weight = models.IntegerField(default=10, verbose_name="权重")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'mx'

    def __str__(self):
        return self.domain


class Txt(models.Model):
    """
    TXT table
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    txttext = models.TextField(max_length=45, verbose_name="TEXT")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'txt'


class Cname(models.Model):
    """
    Cname Table
    """
    cn = models.CharField(max_length=100, verbose_name="别名", unique=True)
    dns = models.CharField(max_length=100, verbose_name="原域名")
    ttl = models.IntegerField(default=10, verbose_name="TTL")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'cname'

    def __str__(self):
        return self.cn


class Alias(models.Model):
    """
    Alias Table
    """
    oldIP = models.GenericIPAddressField(verbose_name="原IP")
    startIP = models.GenericIPAddressField(verbose_name="起始IP")
    endIP = models.GenericIPAddressField(verbose_name="结束IP")
    newIP = models.GenericIPAddressField(verbose_name="新IP")
    ipmask = models.GenericIPAddressField(verbose_name="掩码")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'alias'


class Resolv(models.Model):
    """
    Resolv table
    """
    resolvIP = models.GenericIPAddressField(verbose_name="IP")
    resolvPort = models.IntegerField(blank=True, null=True, verbose_name="端口")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'resolv'

    def __str__(self):
        return str(self.resolvIP)


class MachineRoom(models.Model):
    """
    Machine Romm table
    """
    name = models.CharField(max_length=45, verbose_name="机房名")
    responsible = models.CharField(max_length=45, verbose_name="负责人")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area = models.ForeignKey('Area', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'machineroom'

    def __str__(self):
        return str(self.name)


class IP(models.Model):
    """
    ip table
    """
    ipaddress = models.GenericIPAddressField(verbose_name="IP")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")
    area =  models.ForeignKey("Area", verbose_name="区域")

    class Meta:
        db_table = "ip"


class Domain(models.Model):
    """
    Domain Table
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    createTime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    upTime = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    createUser = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    updateUser = models.CharField(default='now user',max_length=30, verbose_name="更新用户")

    class Meta:
        db_table = "domain"

    def __str__(self):
        return self.domain