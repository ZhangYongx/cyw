# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from dns import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'address', views.AddressViewsSet, base_name='address')
router.register(r'alias', views.AliasViewSet, base_name='alias')
router.register(r'area', views.AreaViewsSetDetail, base_name='area')
router.register(r'cname', views.CnameViewsSet, base_name='cname')
router.register(r'host', views.HostViewsSet, base_name='host')
router.register(r'local', views.LostViewsSet, base_name='local')
router.register(r'mx', views.MxViewsSet, base_name='mx')
router.register(r'ptr', views.PtrViewsSet, base_name='ptr')
router.register(r'server', views.ServerViewsSet, base_name='server')
router.register(r'srv', views.SrvViewsSet, base_name='srv')
router.register(r'txt', views.TxtViewsSet, base_name='txt')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
