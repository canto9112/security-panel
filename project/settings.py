import os
from environs import Env


env = Env()
env.read_env()

HOST = env('HOST')
PORT = env('PORT')
NAME = env('NAME')
USER = env('USER_DB')
PASSWORD = env('PASSWORD_DB')
DEBUG = env.bool('DEBUG_APP')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS_APP = env.list('ALLOWED_HOSTS_APP')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': HOST,
        'PORT': PORT,
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = SECRET_KEY

DEBUG = DEBUG

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ALLOWED_HOSTS_APP


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
