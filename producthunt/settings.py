"""
Django settings for producthunt project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&gn!=!%0hgk!p9bxdoj5k-q=_w5qkfp9-@qn84yo%9yl1^w_xj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'products.apps.ProductsConfig', #installed products
    'accounts.apps.AccountsConfig', #installed accounts
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'producthunt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['producthunt/templates'], #base.html hard coded
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'producthunt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

#replaced database right away
# sudo -u postgres psql

DATABASES = { #set db to postgresql
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'producthuntdb', #CREATE DATABASE
        'USER':'postgres', #easy user and pass to be changed in local_settings.py
        'PASSWORD':'django1234', #easy user and pass to be changed in local_settings.py
        'HOST':'localhost', #valid and to be changed once hosted
        'PORT':'5432' #default port for postgres
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'producthunt/static/') #static directories
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static') #added static root


#settings initialized -> postgresql and .gitignore before runserver
#migrations complete before runserver
#products and accounts installed
#adjusted urls.py
#adjusted products.views
#created home.html as template
#runserver success
#created base.html in core producthunt dir
#adjusted home.html and base.html
#adjusted settings - TEMPLATES 'DIRS'
#adjusted base.html 
#runserver success
#import bootstrap base.html
#removed main class base.html
#created div container base.html
#cleared href in home.html
#added static file location
#added static dirs
#collected static
#adjusted logo
#defined url paths -- producthunt
#defined url paths -- accounts
#created signup.html -- accounts
#created login.html -- accounts
#defined views -- accounts
#user accounts created
#login defined -- accounts
#logout defined -- accounts
#base.html updated