from .base import *

DEBUG = True

# INSTALLED_APPS += [
#     'debug_toolbar',
# ]
ALLOWED_HOSTS += ['localhost', '.herokuapp.com', '127.0.0.1', '0.0.0.0']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db3.sqlite3'),
        }
    }
STATIC_URL = '/static/'
