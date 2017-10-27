<<<<<<< HEAD
"""DnsObject URL Configuration

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
from django.contrib import admin
from django.conf.urls import url,include
=======
# -*- coding: utf-8 -*-
from django.conf.urls import url,include
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6


urlpatterns = [
url(r'^api/', include("dns.urls")),
url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
=======
url(r'^docs/', include_docs_urls(title='DNS管理系统')),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
]
