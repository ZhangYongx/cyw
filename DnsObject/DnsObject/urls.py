# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from rest_framework.authtoken import views
from address.views import AddressViewsSet
from area.views import AreaViewsSet
from users.views import UserViewSet, ChangePassWordViewSet
from cname.views import CnameViewSet
from users import changepawword
from seconddomain.views import SecondDomainViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from django.contrib.auth.decorators import login_required

#注册路由
router = DefaultRouter()
router.register(r'address', AddressViewsSet, base_name='address')
router.register(r'area', AreaViewsSet, base_name='area')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'cname', CnameViewSet, base_name='cname')
router.register(r'seconddomain', SecondDomainViewSet, base_name='seconddomain')
router.register(r'changepassword', ChangePassWordViewSet, base_name='changepassword')

urlpatterns = [

    #url路由
    url(r'^', include(router.urls)),

    #drf登录接口
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #django 自带后台
    url(r'^admin/', admin.site.urls),

    #drf自带的token认证
    url(r'^api-token-auth/', views.obtain_auth_token),

    #drf文档
    url(r'^docs/', include_docs_urls(title='DNS管理系统')),

    #jwt的认证接口
    url(r'^login/', obtain_jwt_token),

    # url(r'^changepwd/$', login_required(changepawword.changepwd), name="changepwd"),
]
