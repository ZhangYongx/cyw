"""jwttest URL Configuration

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
import rf.views as rf_views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token


router = DefaultRouter()
router.register(r'task', rf_views.TaskViewSet, base_name='task')
router.register(r'user', rf_views.UserViewSet, base_name='user')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', obtain_jwt_token),
    url(r'^api-register/', rf_views.CreateUserView.as_view()),
    url(r'^admin/', admin.site.urls),
]
