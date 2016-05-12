"""
Django settings for WeiKe project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yxz1rdwf_s3e%*zee#9*uc(v_=e2m0*fu%7n57*717!5@azt8+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
APPEND_SLASH=False
SESSION_COOKIE_AGE=60*60 *8
SESSION_EXPIRE_AT_BROWSER_CLOSE =True
# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'xadmin',
    'crispy_forms',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'course',
    'accounts',
    'comment'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'WeiKe.urls'

WSGI_APPLICATION = 'WeiKe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


#AUTH_USER_MODEL = "NewUser"
LOGIN_URL = '/accounts/login/'
#HERE = os.path.dirname(os.path.abspath(__file__))
#MEDIA_ROOT = os.path.join(HERE,).replace('\\','/')+'/'
SITE_ROOT=os.path.join(os.path.abspath(os.path.dirname(__file__)),'..')
STATIC_ROOT = os.path.join(SITE_ROOT,'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    ("images", os.path.join(STATIC_ROOT,'images')),
)

MEDIA_ROOT = ''


