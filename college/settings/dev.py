from .common import *

DEBUG = True


SECRET_KEY = 'django-insecure-eo_yjea@jg71_1t&6zbn$za%ty)lsq&hp7bs9ju3^=_-*zoq)p'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'najah',
        'USER': 'root',
        'PASSWORD': 'localhost:3000',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

