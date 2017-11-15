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

from address.views import AddressViewset
from agent.views import AgentViewset
from alias.views import AliasViewset
from area.views import AreaViewset
from cname.views import CnameViewset
from dnsuser.views import DNSUserViewset
from heartbeat.views import HeartbeatViewset
from host.views import HostViewset
from ipinfo.views import IPinfoViewset
from local.views import LocalViewset
from loginfo.views import LoginfoViewset
from mx.views import MxViewset
from ptr.views import PtrViewset
from resolv.views import ResolvViewset
from seconddomain.views import SecondDomainViewset
from server.views import ServerViewset
from srv.views import SrvViewset
from topdomain.views import TopDomainViewset
from txt.views import TxtViewset


router = routers.DefaultRouter()

router.register(r'DNSUser', DNSUserViewset)
router.register(r'Area', AreaViewset)
router.register(r'Agent', AgentViewset)
router.register(r'Ipinfo', IPinfoViewset)
router.register(r'TopDomain', TopDomainViewset)
router.register(r'SecondDomain', SecondDomainViewset)
router.register(r'Host', HostViewset)
router.register(r'Local', LocalViewset)
router.register(r'Server', ServerViewset)
router.register(r'Address', AddressViewset)
router.register(r'Ptr', PtrViewset)
router.register(r'Srv', SrvViewset)
router.register(r'Mx', MxViewset)
router.register(r'Txt', TxtViewset)
router.register(r'Cname', CnameViewset)
router.register(r'Alias', AliasViewset)
router.register(r'Resolv', ResolvViewset)
router.register(r'Loginfo', LoginfoViewset)
router.register(r'Heartbeat', HeartbeatViewset)


urlpatterns = [
    url(r'^dns/', include(router.urls)),
    url(r'dns', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
