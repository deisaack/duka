from .base import *

DEBUG = False

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

ALLOWED_HOSTS = ['mysite.com', ]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

DEFAULT_FROM_EMAIL = "Isaac <deisaack@yahoo.com>"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_PORT = 25
EMAIL_USE_TLS = True


DEFAULT_FILE_STORAGE = 'duka.storage_backends.PublicMediaStorage'
PRIVATE_FILE_STORAGE = 'duka.storage_backends.PrivateMediaStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_KEY'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
import dj_database_url
try:
    db_from_env = dj_database_url.config()
    DATABASES['default'].update(db_from_env)
except:
    pass

STATICFILES_STORAGE = 'duka.storage_backends.StaticStorage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
