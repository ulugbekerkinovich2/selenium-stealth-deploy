import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import django_heroku

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIRS = (os.path.join(BASE_DIR, 'templates'),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-igl2+=ba2#jcmb!o)uxzw&(b#2acg8%*rcj(*xnj@fanwsef4o'
# os.environ['DJANGO_SETTINGS_MODULE'] = 'uploaddata.settings'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://oyster-app-629fq.ondigitalocean.app/', '*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'basic_app',
    'django_cleanup',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uploaddata.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS,
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

WSGI_APPLICATION = 'uploaddata.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# fast-tub
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'railway',
            'USER': 'postgres',
            'PASSWORD': 'CGu8rALao0S3DVlkAQKI',
            'HOST': 'containers-us-west-22.railway.app',
            'PORT': '7053',
        }
        # 'default': {
        #     'ENGINE': 'django.db.backends.postgresql',
        #     'NAME': 'railway',
        #     'USER': 'postgres',
        #     'PASSWORD': 'r7dgmskC5BlTQzBWcc1A',
        #     'HOST': 'containers-us-west-67.railway.app',
        #     'PORT': '6918',
        # }

        # 'default': {
        #     'ENGINE': 'django.db.backends.postgresql',
        #     'NAME': 'd5i0o5nvuf3c8l',
        #     'USER': 'zvsggphcenszqa',
        #     'PASSWORD': '935496f889c0d3937c9ceb19f6aac94ef2070ccea759efd95b4872226f3238ad',
        #     'HOST': 'ec2-3-217-251-77.compute-1.amazonaws.com',
        #     'PORT': '5432',
        # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'postgres7',
    #     'USER': 'postgres',
    #     'PASSWORD': '0852',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, '/staticfiles')
STATIC_URL = 'static/'

STATICFILES = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())
