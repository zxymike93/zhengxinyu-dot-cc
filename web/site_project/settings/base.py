import os
from pathlib import Path

from django.utils.log import DEFAULT_LOGGING


ALLOWED_HOSTS = ['*']

SETTINGS_DIR = Path(__file__).resolve()
BASE_DIR = SETTINGS_DIR.parent.parent.parent

ENVS = {}
lines = open(os.path.join(BASE_DIR, '.env'), 'r').readlines()
for l in lines:
    k, v = l.split('=')
    ENVS[k] = v.strip()

ROOT_URLCONF = 'site_project.urls'

SECRET_KEY = ENVS['SECRET_KEY']

WSGI_APPLICATION = 'site_project.wsgi.application'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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


# Templates & Static files
# https://docs.djangoproject.com/en/1.10/howto/static-files/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

# Upload session
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'images')

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Email
# Set SERVER_EMAIL pointing a smtp server for sending email to admins
ADMINS = (
    ('zxymike93', 'zxymike93@gmail.com'),
)

MANAGERS = ADMINS

SERVER_EMAIL = ENVS['SERVER_EMAIL']

EMAIL_HOST = ENVS['EMAIL_HOST']

EMAIL_PORT = ENVS['EMAIL_PORT']

EMAIL_HOST_USER = ENVS['EMAIL_HOST_USER']

EMAIL_HOST_PASSWORD = ENVS['EMAIL_HOST_PASSWORD']

EMAIL_USE_TLS = True


# Logging
# Using Django's default logging configuration, Plus:
# 1. Console log whether DEBUG=True or DEBUG=False
# 2. Information higher-level than INFO log in file and email_admin
LOGGING = DEFAULT_LOGGING

LOGGING['formatters']['simple'] = {
    'format': '[%(name)s] %(levelname)s: %(message)s'
}
LOGGING['formatters']['full'] = {
    'format': '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
}
LOGGING['handlers']['log_file'] = {
    'level': 'ERROR',
    'class': 'logging.handlers.RotatingFileHandler',
    'filename': './log/error.log',
    'maxBytes': 1048576,
    'backupCount': 20,
    'encoding': 'utf-8',
    'formatter': 'full',
    'filters': ['require_debug_false'],
}

LOGGING['handlers']['console'].pop('filters')

LOGGING['handlers']['console']['formatter'] = 'simple'

LOGGING['loggers']['django']['handlers'].append('log_file')
