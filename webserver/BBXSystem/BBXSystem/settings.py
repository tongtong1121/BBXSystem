"""
Django settings for BBXSystem project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os,sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将当前路径加入到系统索引中
sys.path.insert(0,BASE_DIR)
# 将所有的app统一放在apps文件夹中
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z93b-muj=o=5r7!d5+re@*v4qebe4gwf!9kx(p+5uf=ya0rzy4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# 加入跨域访问允许的端口
ALLOWED_HOSTS = [
'*'
    # 'localhost:8015',
    # '127.0.0.1:8015',
    #
    # '127.0.0.1',
    # '127.0.0.1:8080',
    # 'localhost:8080'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.gis',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #跨域的app
    'corsheaders',
    'bbx',
    'bbxgis',
    # 'gis',
    # 'django.contrib.gis'
]

MIDDLEWARE = [
    # 添加cors
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BBXSystem.urls'
#跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
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

WSGI_APPLICATION = 'BBXSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'NAME': 'bbxsystem',
        # 'NAME': 'bbxsystemgis',
        # 'NAME': 'bbxsys',
        # 现在使用的最新的数据库名称
        # mac
        #'NAME': 'bbx',
        # zw
          'NAME': 'bbxsys',

        # 线上数据库
        # 'NAME': 'BBX',
        # centos
        # 'USER': 'arfu',
        # 'PASSWORD': '@Tongxin321'
        
        # w540
        # 'USER':'root',
        # 'PASSWORD':'123456',

        # p52s
        # 'USER':'root',
        # 'PASSWORD':'123456',
        # 'HOST':'127.0.0.1',

        # mac
        #'USER':'root',
        #'PASSWORD':'12345678',

        # zw
         'USER':'root',
         'PASSWORD':'111111'


        # 'HOST':'127.0.0.1',
        # 'OPTIONS':{'init_command':'SET storage_engine=INNODB;'}
    },
    # 'default': {
    #     'ENGINE': 'django.contrib.gis.db.backends.mysql',
    #     'BACKEND':'django.contrib.gis.db.backends.mysql',
    #     # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     'NAME': 'bbxsystemgis',
    #

    #     # 'HOST':'127.0.0.1',
    #     # 'OPTIONS':{'init_command':'SET storage_engine=INNODB;'}
    # }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
# 设置当前的时区
# TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


# 一些自定义的变量
# 船舶轨迹显示的时间长度
BBX_TRACK_INTERVAL=24

BBX_UTC_INTERVAL=8