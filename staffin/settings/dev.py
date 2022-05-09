import os
from .base import INSTALLED_APPS, MIDDLEWARE, BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3!ymgilcxl6*0c!7h3a*icgvz%n4c&ojx(_@f#!e$$a*+)kimc'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'staffin',
        'USER': 'postgres',
        'PASSWORD': 'beebayk123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = []

INSTALLED_APPS += ['debug_toolbar', 'django_extensions']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INTERNAL_IPS = ["127.0.0.1", ]

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'


CORS_ALLOWED_ORIGINS = (
    'http://localhost:3000',
    'http://127.0.0.1:3000',
)
