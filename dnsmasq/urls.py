# -*- coding: utf-8 -*-
# Author:zhangxun

from django.conf.urls import url, include
from rest_framework import routers
from . import views


# 配置路由
router = routers.DefaultRouter()
router.register(r'UserTable', views.UserTableViewset)
router.register(r'Area', views.AreaViewset)
router.register(r'Agent', views.AgentViewset)
router.register(r'Local', views.LocalViewset)
router.register(r'Server', views.AddressViewset)
router.register(r'HostRecord', views.HostRecordViewset)
router.register(r'Ptr', views.PtrViewset)
router.register(r'Srv', views.SrvViewset)
router.register(r'Mx', views.MxViewset)
router.register(r'Txt', views.TxtViewset)
router.register(r'Cname', views.CnameViewset)
router.register(r'Alias', views.AliasViewset)
router.register(r'Resolv', views.ResolvViewset)
router.register(r'MachineRoom', views.MachineRoomViewset)
router.register(r'IP', views.IPViewset)
router.register(r'Domain', views.DomainViewset)


urlpatterns = [
    # 匹配 URL
    url(r'^', include(router.urls)),
    url(r'dns', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^$', views.index, name="dns"),
]