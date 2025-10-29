import os
from pathlib import Path

# --------------------------------------------------------
# BASE DIRECTORY
# --------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------------
# SECURITY SETTINGS
# --------------------------------------------------------
SECRET_KEY = 'django-insecure-change-this-to-your-own-secret-key'
DEBUG = True
ALLOWED_HOSTS = []

# --------------------------------------------------------
# INSTALLED APPS
# --------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom app
    'listings',
]

# --------------------------------------------------------
# MIDDLEWARE
# --------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------------------------------------------
# URL CONFIGURATION
# --------------------------------------------------------
ROOT_URLCONF = 'alx_travel_app.urls'

# --------------------------------------------------------
# TEMPLATES
# --------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# --------------------------------------------------------
# WSGI
# --------------------------------------------------------
WSGI_APPLICATION = 'alx_travel_app.wsgi.application'

# --------------------------------------------------------
# DATABASE CONFIGURATION
# --------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --------------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------------
# INTERNATIONALIZATION
# --------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------
# STATIC FILES
# --------------------------------------------------------
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --------------------------------------------------------
# EMAIL CONFIGURATION
# --------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'       # or your SMTP server
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'      # replace with your sender email
EMAIL_HOST_PASSWORD = 'your_password_here'      # replace with your password

# --------------------------------------------------------
# CELERY CONFIGURATION (RabbitMQ)
# --------------------------------------------------------
CELERY_BROKER_URL = 'amqp://localhost'  # RabbitMQ broker URL
CELERY_RESULT_BACKEND = 'rpc://'         # RPC backend for results
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

