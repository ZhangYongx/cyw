"""cidszx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from address import views
from agent import views
from alias import views
from area import views
from cname import views
from dnsname import views
from heartbeat import views
from host import views
from ipinfo import views
from local import views
from loginfo import views
from mx import views
from ptr import views
from resolv import views
from seconddomain import views
from server import views
from srv import views
from topdomain import views
from txt import views


router = routers.DefaultRouter()

router.register(r'DNSUser', views.DNSUserViewset)
router.register(r'Area', views.AreaViewset)
router.register(r'Agent', views.AgentViewset)
router.register(r'IPinfo', views.IPinfoViewset)
router.register(r'TopDomain', views.TopDomainViewset)
router.register(r'SecondDomain', views.SecondDomainViewset)
router.register(r'Host', views.HostViewset)
router.register(r'Local', views.LocalViewset)
router.register(r'Server', views.AddressViewset)
router.register(r'Address', views.AddressViewset)
router.register(r'Ptr', views.PtrViewset)
router.register(r'Srv', views.SrvViewset)
router.register(r'Mx', views.MxViewset)
router.register(r'Txt', views.TxtViewset)
router.register(r'Cname', views.CnameViewset)
router.register(r'Alias', views.AliasViewset)
router.register(r'Resolv', views.ResolvViewset)
router.register(r'Loginfo', views.LoginfoViewset)
router.register(r'Heartbeat', views.HeartbeatViewset)


urlpatterns = [
    url(r'^dns/', include(router.urls)),
    url(r'dns', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
