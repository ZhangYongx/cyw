# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Area(models.Model):
    """
    区域表
    """
    area = models.CharField(max_length=45, verbose_name="区域简称")
    area_name = models.CharField(max_length=45, verbose_name="区域")
    responsible = models.CharField(max_length=45, verbose_name="负责人")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")

    class Meta:
        verbose_name = '区域'
        verbose_name_plural = verbose_name
        managed = True
        db_table = 'area'

    def __str__(self):
        return self.area


class Address(models.Model):
    """
    地址详细信息
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    ip = models.GenericIPAddressField(max_length=32, verbose_name="IP地址")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域', related_name='areaid')

    class Meta:
        managed = True
        db_table = 'address'

    def __str__(self):
        return self.domain


class Agent(models.Model):
    Agent_Status = (
        (1, "启用中"),
        (2, "停用中"),
        (3, "暂停"),
    )
    """
    Agent信息
    """
    agent_ip = models.GenericIPAddressField(max_length=32, verbose_name="Agent_IP")
    agent_version = models.CharField(max_length=45, null=True, blank=True, verbose_name="Agent版本")
    agent_statu = models.IntegerField(choices=Agent_Status, verbose_name="Agent状态", help_text="Agent状态")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'agent'


class Alias(models.Model):
    """
    Alias解析
    """
    old_ip = models.GenericIPAddressField(verbose_name="原IP")
    start_ip = models.GenericIPAddressField(verbose_name="起始IP")
    end_ip = models.GenericIPAddressField(verbose_name="结束IP")
    new_ip = models.GenericIPAddressField(verbose_name="新IP")
    mask = models.CharField(max_length=45,verbose_name="掩码")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'alias'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Cname(models.Model):
    """
    Cname解析
    """
    target_domain = models.CharField(max_length=45, verbose_name="别名地址")
    domain = models.CharField(max_length=45,  verbose_name="域名")
    ttl = models.IntegerField(null=True, blank=True, verbose_name="生存周期")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'cname'


class ComputerRoom(models.Model):
    """
    机房信息表
    """
    computer_name = models.CharField(max_length=45, verbose_name="机房")
    responsible = models.CharField(max_length=45, verbose_name="负责人")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    ipinfo = models.ForeignKey('Ipinfo', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'computer_room'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class Doamin(models.Model):

    Domain_level = (
        (2, "二级域名"),
        (3, "三级域名"),
        (4, "四级域名"),
    )
    """
    域名信息表
    """
    id = models.IntegerField(primary_key=True)
    sid = models.IntegerField(null=True, blank=True, verbose_name="次级域名")
    multilevel = models.IntegerField(choices=Domain_level, verbose_name="层级")
    full_domain = models.CharField(max_length=45, verbose_name="完整域名")
    analytic_type = models.CharField(max_length=45, null=True, blank=True, verbose_name="解析类型")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")

    class Meta:
        managed = True
        db_table = 'doamin'


class FDomain(models.Model):
    """
    顶级域名
    """
    domain = models.CharField(max_length=45, verbose_name="顶级域名")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")

    class Meta:
        managed = True
        db_table = 'f_domain'


class HostRecord(models.Model):
    """
    本地解析记录
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    ip = models.GenericIPAddressField(max_length=32, verbose_name="IP")
    ttl = models.CharField(max_length=45, null=True, blank=True, verbose_name="生存周期")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'host-record'


class Ipinfo(models.Model):
    """
    IP信息表
    """
    ip = models.GenericIPAddressField(verbose_name="IP")
    cname = models.IntegerField(verbose_name="别名")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remark = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")

    class Meta:
        managed = True
        db_table = 'ipinfo'


class Local(models.Model):
    """
    本地信息表
    """
    local = models.CharField(max_length=45, verbose_name="本地IP")
    domain = models.CharField(max_length=45, verbose_name="域名")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'local'


class Mx(models.Model):
    """
    mx解析
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    mail_domain = models.CharField(max_length=45, verbose_name="Mx记录值")
    preference = models.IntegerField( verbose_name="优先级")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'mx'


class Ptr(models.Model):
    """
    ptr解析
    """
    ip = models.GenericIPAddressField(max_length=32, verbose_name="IP")
    domain = models.CharField(max_length=45, verbose_name="域名")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'ptr'


class Resolv(models.Model):
    """
    resolv解析
    """
    ip = models.GenericIPAddressField(verbose_name="IP")
    port = models.IntegerField(verbose_name="端口")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注 ")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'resolv'


class SDomain(models.Model):
    """
    二级域名
    """
    fid = models.IntegerField(verbose_name="顶级域名Id")
    domain = models.CharField(max_length=45, verbose_name="域名")
    full_domain = models.CharField(max_length=45, verbose_name="完整域名")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    f_domain = models.ForeignKey(FDomain, models.DO_NOTHING)
    doamin = models.ForeignKey(Doamin, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 's_domain'


class Servere(models.Model):
    """
    服务信息表
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    server_ptr = models.CharField(max_length=32, verbose_name="服务名")
    ip = models.GenericIPAddressField(max_length=32, verbose_name="IP")
    port = models.IntegerField(verbose_name="端口")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'servere'


class Srv(models.Model):
    """
    srv解析
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    server_domain = models.CharField(max_length=45, verbose_name="服务地址")
    port = models.IntegerField(verbose_name="端口")
    priority = models.IntegerField(verbose_name="优先级")
    weight = models.IntegerField(verbose_name="权重")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'srv'


class Txt(models.Model):
    """
    txt解析
    """
    domain = models.CharField(max_length=45, verbose_name="域名")
    mail_domain = models.CharField(max_length=45, verbose_name="mx记录值")
    preference = models.IntegerField(verbose_name="优先级")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")
    create_user = models.CharField(max_length=45, verbose_name="创建者")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")
    area = models.ForeignKey(Area, verbose_name='区域')

    class Meta:
        managed = True
        db_table = 'txt'


class User(models.Model):
    """
    用户信息表
    """

    User_Permission = (
        (1, "普通用户"),
        (2, "管理员"),
        (3, "创建人"),
    )

    username = models.CharField(max_length=45, verbose_name="用户名")
    password = models.CharField(max_length=45, verbose_name="密码")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    permission = models.IntegerField(choices=User_Permission, verbose_name="权限")
    update_user = models.CharField(max_length=45, verbose_name="修改者")
    remarks = models.CharField(max_length=45, null=True, blank=True, verbose_name="备注")

    class Meta:
        managed = True
        db_table = 'user'
