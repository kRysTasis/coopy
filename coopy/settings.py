"""
Django settings for coopy project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import logging
import environ
from socket import gethostname
# from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# try:
#     from .local_settings import *
# except ImportError:
#     pass

HOSTNAME = gethostname()
# dotenv_path = os.path.join(BASE_DIR, '.env')
# load_dotenv(dotenv_path)
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
if 'local' in HOSTNAME:
    # ローカル環境の設定
    DEBUG = env.get_value('DEBUG', cast=bool, default=False)
    SECRET_KEY = env.get_value('SECRET_KEY')
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
    DATABASES = {
        'default': env.db(),
    }

else:
    # 本番環境の設定
    print("本番環境")
    DEBUG = False
    SECRET_KEY = os.environ['SECRET_KEY']
    ALLOWED_HOSTS = ['*']
    import dj_database_url
    db_from_env = dj_database_url.config()
    DATABASES = {
        'default' : dj_database_url.config()
    }
    SESSION_COOLIE_SECURE = True
    CSRF_COOKIE_SECURE = True

if DEBUG:
    logging.basicConfig(
        level = logging.DEBUG,
        format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s:%(lineno)s
        %(message)s''')
else:
    logging.basicConfig(
        level = logging.DEBUG,
        format = '''%(levelname)s %(asctime)s %(pathname)s:%(funcName)s 行数:%(lineno)s:%(lineno)s
        %(message)s'''
        # filename = 'logs/debug.log',
        # filemode = 'a'
    )

# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'userblog.apps.UserblogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coopy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'coopy.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'blog.password_validator.MyCommonPasswordValidator'
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
LOGIN_URL = 'blog:login'
LOGIN_REDIRECT_URL = 'blog:index'

AUTH_USER_MODEL = 'blog.MyUser'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if not DEBUG:
    import django_heroku
    django_heroku.settings(locals())
    del DATABASES['default']['OPTIONS']['sslmode']
