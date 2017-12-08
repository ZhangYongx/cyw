# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from rest_framework.authtoken import views
from address.views import AddressViewsSet
from area.views import AreaViewsSet
from users.views import UserViewSet, ChangePassWordViewSet
from cname.views import CnameViewSet
from alias.views import AliasViewset
from seconddomain.views import SecondDomainViewSet
from host.views import HostViewset
from ipinfo.views import IPinfoViewset
from loginfo.views import LoginfoViewset
from local.views import LocalViewset
from mx.views import MxViewset
from ptr.views import PtrViewset
from resolv.views import ResolvViewset
from server.views import ServerViewset
from srv.views import SrvViewset
from topdomain.views import TopDomainViewset
from txt.views import TxtViewset
from heartbeat.views import HeartBeatViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from agent.views import AgentViewSet
from rest_framework_jwt.views import refresh_jwt_token
# from .views import obtain_expiring_auth_token

# 注册路由
router = DefaultRouter()
router.register(r'address', AddressViewsSet, base_name='address')
router.register(r'area', AreaViewsSet, base_name='area')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'cname', CnameViewSet, base_name='cname')
router.register(r'alias', AliasViewset, base_name='alias')
router.register(r'seconddomain', SecondDomainViewSet, base_name='seconddomain')
router.register(r'changepassword', ChangePassWordViewSet, base_name='changepassword')
router.register(r'heartbeat', HeartBeatViewSet, base_name='heartbeat')
router.register(r'agent', AgentViewSet, base_name='agent')
router.register(r'host', HostViewset, base_name='host')
router.register(r'ipinfo', IPinfoViewset, base_name='ipinfo')
router.register(r'logInfo', LoginfoViewset, base_name='logInfo')
router.register(r'local', LocalViewset, base_name='local')
router.register(r'mx', MxViewset, base_name='mx')
router.register(r'ptr', PtrViewset, base_name='ptr')
router.register(r'resolv', ResolvViewset, base_name='resolv')
router.register(r'server', ServerViewset, base_name='server')
router.register(r'srv', SrvViewset, base_name='srv')
router.register(r'topdomain', TopDomainViewset, base_name='topdoamin')
router.register(r'txt', TxtViewset, base_name='txt')


urlpatterns = [

    # url路由
    url(r'^', include(router.urls)),

    # drf登录接口
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # django 自带后台
    url(r'^admin/', admin.site.urls),

    # drf自带的token认证
    url(r'^api-token-auth/', views.obtain_auth_token),

    # drf文档
    url(r'^docs/', include_docs_urls(title='DNS管理系统')),

    # jwt的认证接口
    url(r'^api_token_register/', obtain_jwt_token),

    # 自定义获取Token
    # url(r'^api/token/', obtain_expiring_auth_token, name='api-token'),

    # 刷新jwt
    url(r'^api-token-refresh/', refresh_jwt_token),

]
