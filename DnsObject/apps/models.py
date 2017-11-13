# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    addr_ip = models.ForeignKey('Ipinfo', models.DO_NOTHING, db_column='addr_ip', unique=True)
    domain = models.CharField(max_length=45)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey('Area', models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'address'


class Agent(models.Model):
    agt_ip = models.CharField(unique=True, max_length=39)
    agt_version = models.CharField(unique=True, max_length=5)
    agt_state = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area_name = models.ForeignKey('Area', models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'agent'


class Alias(models.Model):
    old_ip = models.CharField(max_length=39, blank=True, null=True)
    start_ip = models.CharField(max_length=39, blank=True, null=True)
    end_ip = models.CharField(max_length=39, blank=True, null=True)
    new_ip = models.CharField(max_length=39)
    ipmask = models.CharField(max_length=39)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    uptime = models.DateTimeField(db_column='upTime')  # Field name made lowercase.
    createuser = models.CharField(db_column='createUser', max_length=30)  # Field name made lowercase.
    updateuser = models.CharField(db_column='updateUser', max_length=30)  # Field name made lowercase.
    area_name = models.ForeignKey('Area', models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'alias'


class Area(models.Model):
    name = models.CharField(unique=True, max_length=10)
    fullname = models.CharField(unique=True, max_length=45)
    machine_room = models.CharField(unique=True, max_length=45)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    responsible_name = models.ForeignKey('DnsUser', models.DO_NOTHING, db_column='responsible_name')

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cname(models.Model):
    cname = models.CharField(unique=True, max_length=45)
    domain = models.ForeignKey('SecondDomain', models.DO_NOTHING, db_column='domain', unique=True)
    ttl = models.SmallIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'cname'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class DnsUser(models.Model):
    name = models.CharField(unique=True, max_length=30)
    permission = models.IntegerField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(unique=True, max_length=30)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    remarks = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    qq = models.CharField(max_length=11, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dns_user'


class DnsmasqComojbect(models.Model):
    currentime = models.DateTimeField()
    uptime = models.DateTimeField()
    currentuser = models.CharField(max_length=30)
    upuser = models.CharField(max_length=30)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dnsmasq_comojbect'


class Heartbeat(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.IntegerField()
    agent_ip = models.CharField(max_length=39)
    state = models.IntegerField()
    message = models.CharField(max_length=45, blank=True, null=True)
    agent_version = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'heartbeat'


class Host(models.Model):
    domain = models.ForeignKey('SecondDomain', models.DO_NOTHING, db_column='domain', unique=True)
    host_ip = models.ForeignKey('Ipinfo', models.DO_NOTHING, db_column='host_ip', unique=True)
    ttl = models.SmallIntegerField()
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'host'


class Ipinfo(models.Model):
    ipaddress = models.CharField(unique=True, max_length=39)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'ipinfo'


class Local(models.Model):
    domain = models.CharField(unique=True, max_length=45)
    host_ip = models.ForeignKey(Host, models.DO_NOTHING, db_column='host_ip', unique=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'local'


class Loginfo(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.IntegerField()
    state = models.IntegerField()
    message = models.CharField(max_length=10, blank=True, null=True)
    agent_ip = models.CharField(unique=True, max_length=39)

    class Meta:
        managed = False
        db_table = 'loginfo'


class Mx(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.ForeignKey('SecondDomain', models.DO_NOTHING, db_column='domain', unique=True)
    mx_domain = models.CharField(max_length=45)
    priority = models.IntegerField()
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'mx'


class Ptr(models.Model):
    ptr_ip = models.ForeignKey(Ipinfo, models.DO_NOTHING, db_column='ptr_ip', unique=True)
    domain = models.ForeignKey('SecondDomain', models.DO_NOTHING, db_column='domain', unique=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'ptr'


class Resolv(models.Model):
    resolv_ip = models.CharField(max_length=39)
    resolv_port = models.SmallIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name')

    class Meta:
        managed = False
        db_table = 'resolv'


class SecondDomain(models.Model):
    domain = models.CharField(unique=True, max_length=45)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    remarks = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'second_domain'


class Server(models.Model):
    domain = models.ForeignKey(SecondDomain, models.DO_NOTHING, db_column='domain', unique=True)
    reverse_ip = models.CharField(db_column='reverse _ip', max_length=39)  # Field renamed to remove unsuitable characters.
    nameserver_ip = models.CharField(max_length=39)
    nameserver_port = models.SmallIntegerField()
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'server'


class Srv(models.Model):
    domain = models.ForeignKey(SecondDomain, models.DO_NOTHING, db_column='domain', unique=True)
    srv_domain = models.CharField(max_length=45)
    srv_port = models.SmallIntegerField()
    priority = models.IntegerField()
    weight = models.IntegerField()
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'srv'


class Topdomain(models.Model):
    id = models.IntegerField(primary_key=True)
    top_domain = models.CharField(unique=True, max_length=45)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    del_user = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'topdomain'


class Txt(models.Model):
    domain = models.ForeignKey(SecondDomain, models.DO_NOTHING, db_column='domain', unique=True)
    text = models.TextField()
    remarks = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    create_user = models.CharField(max_length=30)
    update_user = models.CharField(max_length=30)
    area_name = models.ForeignKey(Area, models.DO_NOTHING, db_column='area_name', unique=True)

    class Meta:
        managed = False
        db_table = 'txt'
