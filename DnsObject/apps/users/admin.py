# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from users.models import DnsUserProfile
from django.contrib.auth import get_user_model

# User = get_user_model()
#
#
# class UserProfileInline(admin.StackedInline):
#     model = DnsUserProfile
#     fk_name = 'user'
#     max_num = 1
#
#
# class UserProfileAdmin(DnsUserProfile):
#     inlines = [UserProfileInline, ]
#
#
# admin.site.register(User, UserProfileAdmin)