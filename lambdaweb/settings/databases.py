import os

import env
import paths
import secrets


if env.DEV_ENV:
    database_dir = os.path.join(paths.BASE_PATH, 'databases')

    if not os.path.exists(database_dir):
        os.mkdir(database_dir)

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(database_dir, 'sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': secrets.DATABASE_USER,
            'PASSWORD': secrets.DATABASE_PASSWORD,
            'HOST': secrets.DATABASE_HOST,
            'PORT': secrets.DATABASE_PORT,
        }
    }
