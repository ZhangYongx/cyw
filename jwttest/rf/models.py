# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise u'邮箱地址不能为空'
        user = self.model(email=self.normalize_email(email), last_login=timezone.now())
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True, max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email


class Task(models.Model):
    title = models.CharField(max_length=100)
    person = models.ForeignKey(User, related_name='tasks')
    dut_to = models.DateTimeField()

    def __str__(self):
        return self.title