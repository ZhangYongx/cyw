# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from rest_framework.authtoken import views


urlpatterns = [

url(r'^api/', include("dns.urls")),
url(r'^admin/', admin.site.urls),
url(r'^api-token-auth/', views.obtain_auth_token),
url(r'^docs/', include_docs_urls(title='DNS管理系统')),
]
