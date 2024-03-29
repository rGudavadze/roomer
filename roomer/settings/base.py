"""
Django settings for roomer project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

from apps.utils import secret_manager

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

if os.environ.get("DJANGO_SETTINGS_MODULE") in ["roomer.settings.test", "roomer.settings.dev-local"]:
    ENVS = os.environ

else:
    secret_manager = secret_manager.SecretManagerClient()
    ENVS = secret_manager.get_secret_data()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENVS.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = "users.User"

# Application definition

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "django_filters",
    "django_celery_beat",
]

OUR_APPS = [
    "apps.base",
    "apps.app_helpers",
    "apps.users",
    "apps.rooms",
    "apps.booking",
]

INSTALLED_APPS = (
    [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    + THIRD_PARTY_APPS
    + OUR_APPS
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "roomer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "roomer.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": ENVS.get("DATABASE_NAME"),
        "USER": ENVS.get("DATABASE_USER"),
        "PASSWORD": ENVS.get("DATABASE_PASSWORD"),
        "HOST": ENVS.get("DATABASE_HOST"),
        "PORT": ENVS.get("DATABASE_PORT"),
    }
}

# Celery broker configurations
CELERY_BROKER_URL = "amqp://{username}:{password}@{host}:{port}/".format(
    username=ENVS.get("RABBITMQ_USER"),
    password=ENVS.get("RABBITMQ_PASS"),
    host=ENVS.get("RABBITMQ_HOST"),
    port=ENVS.get("RABBITMQ_PORT"),
)
CELERY_RESULT_BACKEND = "rpc://{username}:{password}@{host}:{port}/".format(
    username=ENVS.get("RABBITMQ_USER"),
    password=ENVS.get("RABBITMQ_PASS"),
    host=ENVS.get("RABBITMQ_HOST"),
    port=ENVS.get("RABBITMQ_PORT"),
)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

FIXTURE_DIRS = ["fixtures"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Roomer",
    "DESCRIPTION": "Book a room in the office",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"custom_formatter": {"format": "[{asctime}] {levelname} {message}", "style": "{"}},
    "handlers": {
        "custom_handler": {"class": "logging.StreamHandler", "formatter": "custom_formatter"},
        "file": {
            "class": "logging.FileHandler",
            "filename": "info.log",
            "formatter": "custom_formatter",
        },
    },
    "loggers": {
        "logger": {
            "handlers": ["custom_handler", "file"],
            "level": "INFO",
        }
    },
}
