from datetime import timedelta
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-!-73#qx8msma^+az0yi$tz%sha-n4#=)zw2cb5-l5&7!xo-n91"

DEBUG = True

ALLOWED_HOSTS = ["*"]
AUTH_USER_MODEL = "authentication.CustomUser"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_yasg",
    "rest_framework_simplejwt",
    "rest_framework.authtoken",
    "corsheaders",
    # local apps
    "tenants.apps.TenantsConfig",
    "authentication.apps.AuthenticationConfig",
    "agents.apps.AgentsConfig",
    "properties.apps.PropertiesConfig",
    "communication.apps.CommunicationConfig",
    "maintenance.apps.MaintenanceConfig",
    "landlords.apps.LandlordsConfig",
    "payments.apps.PaymentsConfig",
    "company.apps.CompanyConfig",
    "client.apps.ClientConfig",
    "vacate.apps.VacateConfig",
    "utils.apps.UtilsConfig",
    "stats.apps.StatsConfig",
    "expenses.apps.ExpensesConfig",
]
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "x-csrftoken",
]
CORS_ALLOW_ALL_ORIGINS = True  # Enable all origins, not recommended in production
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "OPTIONS",
    "DELETE",
    "PUT",
    "PATCH",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "Rentoo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

WSGI_APPLICATION = "Rentoo.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# rest_framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}
# JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_LIFETIME": timedelta(days=30),
    "SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER": timedelta(days=1),
}
