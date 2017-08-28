import os
from decouple import config
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
ADMINS = config('ADMINS')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])
AUTH_USER_MODEL = 'authtools.User'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRISPY_TEMPLATE_PACK = 'bootstrap3'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PWD_KEY'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
DEBUG = config('DEBUG', cast=bool)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
# GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyD2XP6khyd123inKasJ2NxfWodaqYO_HqY'
GEOPOSITION_GOOGLE_MAPS_API_KEY = config('GEOPOSITION_GOOGLE_MAPS_API_KEY')
GOOGLE_RECAPTCHA_SECRET_KEY = config('GOOGLE_RECAPTCHA_SECRET_KEY')
INSTALLED_APPS = [
    'rest_framework',

    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'duka.accounts',
    'duka.profiles',
    'duka.favorites',

    'crispy_forms',
    'authtools',
    'braces',
    'easy_thumbnails',
    'geoposition',
]
LANGUAGE_CODE = 'en-us'
LIVE_DIR = os.path.join(BASE_DIR, "live")
LOGIN_REDIRECT_URL = reverse_lazy("home")
LOGIN_URL = reverse_lazy("accounts:login")
MANAGERS = ADMINS
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(LIVE_DIR, 'live/media')
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
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
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 6
}
ROOT_URLCONF = 'duka.urls'
SECRET_KEY = config('SECRET_KEY')
SITE_ID = 1
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(LIVE_DIR, "static")
STATIC_URL = '/static/'
THUMBNAIL_EXTENSION = 'png'
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
TIME_ZONE = 'Africa/Nairobi'
USE_L10N = True
USE_I18N = True
USE_TZ = True
WSGI_APPLICATION = 'duka.wsgi.application'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db3.sqlite3'),
        }
    }
if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travisci',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }