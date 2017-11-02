from .base import *
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

print("estoy en produccion")

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOST = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
        'NAME': os.environ.get('DB_SCHEMA'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD:': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '3306',
    }
}