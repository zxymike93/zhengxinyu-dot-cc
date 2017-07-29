from .base import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'zhengxinyu',
        'USER': ENVS['DB_USER'],
        'PASSWORD': ENVS['DB_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
