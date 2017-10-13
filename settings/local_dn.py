# -*- encoding: utf-8 -*-
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

ADMINS = (('M.G.', 'cappuccio@silvercube.pl'), ('D.N.', 'dnowak@silvercube.pl'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rigipstrophy',
        'USER': 'zdalny',
        'PASSWORD': '123123',
        'HOST': 'localhost',
        'PORT': '',
    },
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.silvercube.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@silvercube.pl'
EMAIL_HOST_PASSWORD = 'fUcUwAuE'
EMAIL_FROM_USER = 'Rigips Throphy <noreply@silvercube.pl>'