# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from rest_framework.authtoken import views
from address.views import AddressViewsSet
from area.views import AreaViewsSet
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'address', AddressViewsSet, base_name='address')
router.register(r'area', AreaViewsSet, base_name='area')
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [

    url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', admin.site.urls),

    #drf自带的token认证
    url(r'^api-token-auth/', views.obtain_auth_token),

    #drf文档
    url(r'^docs/', include_docs_urls(title='DNS管理系统')),

    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),
]
