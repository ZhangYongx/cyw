# -*- coding: utf-8 -*-
# Author:zhangxun

from django.conf.urls import url, include
from rest_framework import routers
from . import views


# 配置路由
router = routers.DefaultRouter()
router.register(r'Alias', views.AliasViewset)
router.register(r'Cname', views.CnameViewset)
router.register(r'Are', views.AreaViewset)

urlpatterns = [
    # 匹配 URL
    url(r'^', include(router.urls)),
    url(r'dns', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^$', views.index, name="dns"),
]