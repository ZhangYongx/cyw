# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.


# class ComObject(models.Model):
#     """
#     各表常用字段
#     """
#     current_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
#     update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
#     current_user = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
#     update_user = models.CharField(default='now user',max_length=30, editable=False, verbose_name="更新用户")
#     remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
#
#     class Meta:
#         abstract = True


class DNSUser(models.Model):
    """
    User Table
    """
    permission_choice = (
        (0, "普通用户"),
        (1, "管理员"),
        (2, "超级管理员"),
    )

    username = models.CharField(max_length=30, blank=False, null=False, unique=True, verbose_name="用户名")
    permission = models.IntegerField(choices=permission_choice, default=0, verbose_name="权限")
    email = models.EmailField(max_length=30, blank=False, null=False, verbose_name="邮箱地址")
    qq = models.CharField(max_length=11, null=False, verbose_name="QQ号")
    phone = models.CharField(max_length=11, null=False, verbose_name="手机号")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    update_user = models.CharField(default='now user',max_length=30, editable=False, verbose_name="更新用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")


    class Meta:
        db_table = 'dnsuser'

    def __str__(self):
        return self.username


class Area(models.Model):
    """
    Area Table
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="区域简称", help_text="请填写区域的英文缩写")
    fullname = models.CharField(max_length=45, unique=True, blank=False, verbose_name="区域名")
    machine_name = models.CharField(max_length=45, unique=True, blank=False, null=False, verbose_name="机房名")
    responsible = models.ForeignKey(DNSUser, to_field='username', verbose_name="负责人")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")

    class Meta:
        # managed = True
        db_table = 'area'

    def __str__(self):
        return self.name


class Agent(models.Model):
    """
    Agent Table
    """
    live_states = (
        (0, "running"),
        (1, "down"),
        (2, "pause"),
        (3, "unknown"),
    )
    agt_ip = models.GenericIPAddressField(verbose_name="代理IP")
    agt_version = models.IntegerField(default=1, verbose_name="版本")
    agt_states = models.IntegerField(choices=live_states, default=1, verbose_name="运行状态")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")

    class Meta:
        db_table = 'agent'
        unique_together = ('agt_ip', 'area_name')

    def __str__(self):
        return str(self.agtIP)


class IPinfo(models.Model):
    """
    ip table
    """
    ipaddress = models.GenericIPAddressField(blank=False, null=False, unique=True, verbose_name="IP")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")

    class Meta:
        db_table = "ipinfo"

    def __str__(self):
        return self.ipaddress


class TopDomain(models.Model):
    """
    顶级域名
    """
    top_domain = models.CharField(max_length=45, unique=True, verbose_name="顶级域名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    delete_user = models.CharField(default='now user', editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        db_table = 'topdomain'

    def __str__(self):
        return self.top_domain


class SecondDomain(models.Model):
    """
    次级域名
    """
    domain = models.CharField(max_length=45, unique=True, verbose_name="次级域名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user',max_length=30, editable=False, verbose_name="更新用户")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        db_table = "second_domain"

    def __str__(self):
        return self.domain


class Host(models.Model):
    """
    主机记录
    """
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    host_ip = models.ForeignKey(IPinfo, to_field='ipaddress', verbose_name="IP地址")
    ttl = models.IntegerField(default=600, verbose_name="TTL")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")

    class Meta:
        # managed = True
        unique_together = ('host_ip', 'domain', 'area_name')
        db_table = 'host'

    def __str__(self):
        return self.domain


class Local(models.Model):
    """
    Local Table
    """
    domain = models.CharField(max_length=45, verbose_name="本地域名")
    ipaddress = models.ForeignKey(IPinfo, to_field='ipaddress', verbose_name="主机")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")


    class Meta:
        db_table = "local"
        unique_together = ('ipaddress', 'area_name')

    def __str__(self):
        return self.domain


class Server(models.Model):
    """
    Server Table
    """
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    reverse_ip = models.GenericIPAddressField(verbose_name="反向IP")
    nameserver_ip = models.GenericIPAddressField(verbose_name="NS IP", help_text="请输入域名服务器的")
    nameserver_port = models.IntegerField(default=53, verbose_name="NS PORT", help_text="请输入域名服务器的端口")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user',max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")

    class Meta:
        db_table = "server"
        unique_together = ('reverse_ip', 'area_name')

    def __str__(self):
        return self.domain


class Address(models.Model):
    """
    Address Table
    """
    addr_ip = models.ForeignKey(IPinfo, to_field='ipaddress', verbose_name="IP 地址")
    domain = models.CharField(max_length=45, verbose_name="域名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user',max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'address'
        unique_together = ('addr_ip', 'area_name')

    def __str__(self):
        return str(self.addr_ip)


class Ptr(models.Model):
    """
    PTR table
    """
    ptr_ip = models.ForeignKey(IPinfo, to_field='ipaddress', verbose_name="IP")
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'ptr'
        unique_together = ('domain', 'area_name')

    def __str__(self):
        return str(self.ptr_ip)


class Srv(models.Model):
    """
    SRV Table
    """
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    srv_domain = models.CharField(max_length=45, null=False, verbose_name="服务地址")
    srv_port = models.IntegerField(verbose_name="端口")
    priority = models.IntegerField(default=10, verbose_name="优先级")
    weight = models.IntegerField(default=10, verbose_name="权重")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'srv'
        unique_together = ('srv_domain', 'area_name')

    def __str__(self):
        return self.domain


class Mx(models.Model):
    """
    mail server table
    """
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    mxDomain = models.EmailField(max_length=45, verbose_name="服务地址")
    priority = models.IntegerField(default=10, verbose_name="权重")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user',max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'mx'
        unique_together = ('mxDomain', 'area_name')

    def __str__(self):
        return self.domain


class Txt(models.Model):
    """
    TXT table
    """
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    text = models.TextField(max_length=45, verbose_name="TEXT")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user', editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user', max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'txt'
        unique_together = ('domain', 'area_name')


class Cname(models.Model):
    """
    Cname Table
    """
    cname = models.CharField(max_length=100, verbose_name="别名")
    domain = models.ForeignKey(SecondDomain, to_field='domain', verbose_name="域名")
    ttl = models.IntegerField(default=10, verbose_name="TTL")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user',max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'cname'
        unique_together = ('cname', 'area_name')

    def __str__(self):
        return self.cname


class Alias(models.Model):
    """
    Alias Table
    """
    old_ip = models.GenericIPAddressField(default='169.254.7.1', blank=True, null=True, verbose_name="原IP")
    start_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="起始IP")
    end_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="结束IP")
    new_ip = models.GenericIPAddressField(verbose_name="新IP")
    ipmask = models.GenericIPAddressField(verbose_name="掩码")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user',max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey(Area, to_field='name', verbose_name="区域")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")

    class Meta:
        # managed = True
        db_table = 'alias'
        unique_together = ('new_ip', 'area_name')


class Resolv(models.Model):
    """
    Resolv table
    """
    resolv_ip = models.GenericIPAddressField(verbose_name="IP")
    resolv_port = models.IntegerField(blank=True, null=True, verbose_name="端口")
    remarks = models.CharField(max_length=45, blank=True, null=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    create_user = models.CharField(default='now user',editable=False, max_length=30, verbose_name="创建用户")
    update_user = models.CharField(default='now user',max_length=30, editable=False, verbose_name="更新用户")
    area_name = models.ForeignKey('Area', to_field='name', verbose_name="区域")

    class Meta:
        # managed = True
        db_table = 'resolv'
        unique_together = ('resolv_ip', 'area_name')

    def __str__(self):
        return str(self.resolv_ip)


class Loginfo(models.Model):
    """
    日志表
    """
    log_state = (
        (0, '正常'),
        (1, '错误'),
        (2, 'unknown'),
    )
    time = models.IntegerField(unique=True, verbose_name="时间戳")
    state = models.IntegerField(choices=log_state, default=0, verbose_name="状态")
    agent_ip = models.GenericIPAddressField(verbose_name="Agent IP")
    message = models.CharField(max_length=10, blank=True, null=True, verbose_name="信息保留")

    class Meta:
        db_table = "Loginfo"


class Heartbeat(models.Model):
    """
    心跳表
    """
    heart_state = (
        (0, '正常'),
        (1, '告警'),
        (2, '错误'),
    )
    time = models.IntegerField(unique=True, verbose_name="时间戳")
    state = models.IntegerField(choices=heart_state, default=0, verbose_name="状态")
    agent_ip = models.GenericIPAddressField(verbose_name="Agent IP")
    message = models.CharField(max_length=10, blank=True, null=True, verbose_name="信息保留")

    class Meta:
        db_table = "Heartbeat"