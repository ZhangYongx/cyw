# -*- coding: utf-8 -*-
# Author:zhangxun

from django.conf.urls import url, include
from . import views


urlpatterns = [
    # app name dns
    url(r'^$', views.index, name="dns"),
]