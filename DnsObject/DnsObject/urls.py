# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls
from django.contrib import admin


urlpatterns = [
url(r'^api/', include("dns.urls")),
url(r'^admin/', admin.site.urls),
url(r'^docs/', include_docs_urls(title='DNS管理系统')),
]
