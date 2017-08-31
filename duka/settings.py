import os
from decouple import config
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
ADMINS = (
  ('Prof. Isaac', 'deisaack@gmail.com'),
)
ALLOWED_HOSTS= ['localhost', '.herokuapp.com', '127.0.0.1', '0.0.0.0', 'duka.herokuapp.com']
AUTH_USER_MODEL = 'authtools.User'
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'


AWS_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'duka.storage_backends.StaticStorage'

AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'duka.storage_backends.PublicMediaStorage'

AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'duka.storage_backends.PrivateMediaStorage'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRISPY_TEMPLATE_PACK = 'bootstrap3'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_KEY'),
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }
# import dj_database_url
# db_from_env = dj_database_url.config()
# DATABASES['default'].update(db_from_env)
DEBUG = config('DEBUG', cast=bool)
DEFAULT_FROM_EMAIL = "Isaac <deisaack@yahoo.com>"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_PORT = 25
EMAIL_USE_TLS = True
# GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyD2XP6khyd123inKasJ2NxfWodaqYO_HqY'
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCKKERHiiwDU37DQ719Uj93bXVlSGRMn9U'
# GEOPOSITION_GOOGLE_MAPS_API_KEY = config('GEOPOSITION_GOOGLE_MAPS_API_KEY')
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
    'storages',
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
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_ROOT = os.path.join(LIVE_DIR, "static")
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATIC_URL = '/static/'
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