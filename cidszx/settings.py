# -*- coding: utf-8 -*-
"""
Django settings for cidszx project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# solve the Error: could not found DJANGO_SETTINGS_MODULE
# path = 'D:\\pyProject\\cidszx\\cidszx'
# if path not in sys.path:
#     sys.path.append(path)
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cidszx.settings")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_erdb9qji&b3sq^qrb4zbi(jfzp!@k#o(q!0fjwe9qdh_-t&6m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'dnsuser.apps.DnsuserConfig',
    'agent.apps.AgentConfig',
    'area.apps.AreaConfig',
    'topdomain.apps.TopdomainConfig',
    'seconddomain.apps.SeconddomainConfig',
    'ipinfo.apps.IpinfoConfig',
    'address.apps.AddressConfig',
    'alias.apps.AliasConfig',
    'host.apps.HostConfig',
    'cname.apps.CnameConfig',
    'local.apps.LocalConfig',
    'mx.apps.MxConfig',
    'ptr.apps.PtrConfig',
    'resolv.apps.ResolvConfig',
    'server.apps.ServerConfig',
    'srv.apps.SrvConfig',
    'txt.apps.TxtConfig',
    'heartbeat.apps.HeartbeatConfig',
    'loginfo.apps.LoginfoConfig',

]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    # 'DEFAULT_PAGINATION_CLASS':[
    #     'rest_framework.pagination.PageNumberPagination',
    # ],
    # 'PAGE_SIZE': 10,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cidszx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


WSGI_APPLICATION = 'cidszx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cidszx',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

# 后台统一使用 UTC 的时间存储，web显示为本地时间由前端来处理。
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
