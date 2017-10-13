# -*- encoding: utf-8 -*-
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['trophy.rigips.pl']

ADMINS = (('M.G.', 'cappuccio@silvercube.pl'), ('D.N.', 'dnowak@silvercube.pl'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'd11trophy18',
        'USER': 'u11trophy',
        'PASSWORD': 'n2084fonlEfFQax5',
        'HOST': '192.168.12.91',
        'PORT': '',
    },
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.silvercube.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@silvercube.pl'
EMAIL_HOST_PASSWORD = 'fUcUwAuE'
EMAIL_FROM_USER = 'Rigips Throphy <noreply@silvercube.pl>'