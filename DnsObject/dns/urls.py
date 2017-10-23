# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from dns import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'address', views.AddressViewsSet)
router.register(r'addressall', views.AddressViewsSetDetail)
router.register(r'alias', views.AliasViewSet)
router.register(r'area', views.AreaViewsSetDetail)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]