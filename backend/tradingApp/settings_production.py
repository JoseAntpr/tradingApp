import os
from tradingApp.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

ADMINS = ((
	os.environ.get('ADMIN_EMAIL_NAME', ''), 
	os.environ.get('ADMIN_EMAIL_ADDRESS', '')
),)

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'HOST': 'localhost',
       'NAME': 'tradinapp',
       'USER': 'ebury',
       'PASSWORD': 'ebury'
   }
}
