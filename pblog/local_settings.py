import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-=_1_yaa_#g3=+@3n&=z@n(e5azv@10j@(y%v4c4g(8$5c3rpws'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
