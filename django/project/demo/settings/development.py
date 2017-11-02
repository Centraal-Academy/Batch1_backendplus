from .base import *
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

print("estoy en development")
DEBUG = os.environ.get('DEBUG_DEV')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
        'NAME': os.environ.get('DB_SCHEMA_DEV'),
        'USER': os.environ.get('DB_USER_DEV'),
        'PASSWORD': os.environ.get('DB_PASSWORD_DEV'),
        'HOST': os.environ.get('DB_HOST_DEV'),
        'PORT': '3306',
    }
}