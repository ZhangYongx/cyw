# -*- coding: utf-8 -*-
"""
Django settings for DnsObject project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = '9$w^(3(6!!p@077ol38s#x*!8%%@o8=kq0a4#*qp6a_(s5apan'

DEBUG = True

ALLOWED_HOSTS = ['*',]

AUTH_USER_MODEL = 'users.DnsUserProfile'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'address.apps.AddressConfig',
    'area.apps.AreaConfig',
    'users.apps.UsersConfig',
    'cname.apps.CnameConfig',
    'heartbeat.apps.HertbeatConfig',
    'seconddomain.apps.SeconddomainConfig',
    'agent.apps.AgentConfig',
    'alias.apps.AliasConfig',
    'host.apps.HostConfig',
    'ipinfo.apps.IpinfoConfig',
    'local.apps.LocalConfig',
    'loginfo.apps.LoginfoConfig',
    'mx.apps.MxConfig',
    'ptr.apps.PtrConfig',
    'resolv.apps.ResolvConfig',
    'server.apps.ServerConfig',
    'srv.apps.SrvConfig',
    'topdomain.apps.TopdomainConfig',
    'txt.apps.TxtConfig',
    'corsheaders',
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'DnsObject.urls'

AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)

# 模板文件
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DnsObject.wsgi.application'


# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dnsdb',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'init_command': 'SET storage_engine=INNODB;'}
    }
}

# validators密码认证
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 时区、语言设置
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# 设置为本地时间
USE_TZ = False

# 引入REST_FRAMEWORK
REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication'
    ),
}


# REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES = 60

# JWT认证，token过期时间
import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

# 手机号码正则表达式
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"

STATIC_URL = '/static/'
