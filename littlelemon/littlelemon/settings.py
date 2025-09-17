# settings.py

import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- SECURITY SETTINGS FOR PRODUCTION ---

# Get the secret key from an environment variable.
# NEVER keep the secret key in the code in production!
SECRET_KEY = os.environ.get('SECRET_KEY')

# DEBUG is False in production, and True in development.
# Render sets the 'RENDER' environment variable.
DEBUG = 'RENDER' not in os.environ

# --- ALLOWED HOSTS & CSRF SETTINGS ---

ALLOWED_HOSTS = []

# Get the hostname from the 'RENDER_EXTERNAL_HOSTNAME' environment variable
# that is automatically set by Render.
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# This is the line that fixes your CSRF "Forbidden (403)" error.
# It tells Django to trust requests from your Render app's domain.
# Make sure to replace 'testdjangolemonade.onrender.com' with your actual app name.
CSRF_TRUSTED_ORIGINS = ['https://testdjangolemonade.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Add whitenoise to serve static files
    'whitenoise.runserver_nostatic',
    'restaurant',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Add WhiteNoiseMiddleware right after the security middleware.
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'littlelemon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['restaurant/templates' ],
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

WSGI_APPLICATION = 'littlelemon.wsgi.application'


# --- DATABASE SETTINGS FOR PRODUCTION ---

# Use dj-database-url to parse the DATABASE_URL environment variable
# provided by Render's PostgreSQL service.
# For local development, it will fall back to your sqlite3 database.
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# The settings for media files have been updated for the Graded assessment
MEDIA_URL = '/media/'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- STATIC FILES SETTINGS FOR PRODUCTION ---
STATIC_URL = '/static/'

# This is where Django will collect all static files.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Tell WhiteNoise to use a more efficient compression algorithm.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "restaurant/static"),
]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
