import os
from pathlib import Path
import smtplib

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o7m27-a3s6l8q8)1sf^ll39ykm(10n9zn$1337(d08)=tagztz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'company',
    'customers',
    'guidance',
    'job',
    'homeapp',
    'ckeditor',
    'jazzmin',
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Keep the default backend
    'customers.backends.EmailBackend',  # Add your custom backend
]


ROOT_URLCONF = 'NewbieOs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'customers.context_processors.user_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewbieOs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newbieos',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR,  'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    'site_header': 'NewbieOs Admin',
    'site_brand': 'NewbieOs',
    'site_logo': 'images/logo.png',
    "welcome_sign": "Welcome to the admin dashboard",
    "show_ui_builder": True,
    "navigation_expanded": True,  
    }


CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 800,
        'skin': 'moono',
        'codeSnippet_theme': 'monokai',
        'extraPlugins': ','.join([
            'codesnippet', 'widget', 'lineutils', 'clipboard', 
            'dialog', 'dialogui', 'contextmenu', 'autogrow', 
            'exportfile', 'filebrowser', 'html5filebrowser', 
            'image', 'image2', 'imagebrowser', 'imageupload', 
            'smiley', 'template', 'templatestyles', 'toolbar'
        ]),
    }
}


LOGIN_URL = 'signup'


AUTO_LOGOUT = {
    'IDLE_TIME': 15 * 60,  
    'MESSAGE': 'The session has expired. Please login again to continue.',
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'goldennaina2020ad@gmail.com'
EMAIL_HOST_PASSWORD = 'vyah gyjc flks oeyj'
DEFAULT_FROM_EMAIL = 'goldennaina2020ad@gmail.com'
ADMIN_EMAIL = 'goldennaina2020.manager@gmail.com'  

try:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    print("SMTP connection successful")
    server.quit()
except Exception as e:
    print(f"SMTP connection failed: {e}")


