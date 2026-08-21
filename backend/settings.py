"""
Django settings for backend project.

Production-ready configuration for Render deployment.
Django 4.2.x
"""

from pathlib import Path
import os

import dj_database_url


# ============================================================
# BASE DIRECTORY
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY
# ============================================================

# IMPORTANT:
# Never hard-code SECRET_KEY in production.
# Set SECRET_KEY in Render Environment Variables.

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-development-only-change-this-key"
)

# Render Environment Variable:
# DEBUG=False
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"


# ============================================================
# ALLOWED HOSTS
# ============================================================

ALLOWED_HOSTS = [
    "api.spsengineeringsolutions.site",
    "spsengineeringsolutions.site",
    "www.spsengineeringsolutions.site",
    ".onrender.com",
    "localhost",
    "127.0.0.1",
]


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [
    # Jazzmin
    "jazzmin",

    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third Party
    "rest_framework",
    "corsheaders",

    # Local Apps
    "careers",
    "applications",
    "contact",
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise for static files
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ============================================================
# URL CONFIGURATION
# ============================================================

ROOT_URLCONF = "backend.urls"


# ============================================================
# TEMPLATES
# ============================================================

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


# ============================================================
# WSGI
# ============================================================

WSGI_APPLICATION = "backend.wsgi.application"


# ============================================================
# DJANGO REST FRAMEWORK
# ============================================================

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}


# ============================================================
# CORS
# ============================================================

# Production frontend
CORS_ALLOWED_ORIGINS = [
    "https://spsengineeringsolutions.site",
    "https://www.spsengineeringsolutions.site",
]

# Local development
if DEBUG:
    CORS_ALLOWED_ORIGINS += [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]


# ============================================================
# CSRF
# ============================================================

CSRF_TRUSTED_ORIGINS = [
    "https://spsengineeringsolutions.site",
    "https://www.spsengineeringsolutions.site",
    "https://api.spsengineeringsolutions.site",
]

if DEBUG:
    CSRF_TRUSTED_ORIGINS += [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]


# ============================================================
# JAZZMIN
# ============================================================

JAZZMIN_SETTINGS = {
    "site_title": "SPS Solutions Admin",
    "site_header": "SPS Solutions",
    "site_brand": "SPS Solutions",
    "welcome_sign": "Welcome to SPS Solutions Admin",
    "copyright": "SPS Solutions",

    "search_model": [
        "careers.Career",
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "careers.Career": "fas fa-briefcase",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    "topmenu_links": [
        {
            "name": "Dashboard",
            "url": "admin:index",
            "permissions": ["auth.view_user"],
        },
        {
            "name": "Career Openings",
            "url": "admin:careers_career_changelist",
        },
    ],

    "usermenu_links": [
        {
            "name": "SPS Website",
            "url": "/",
            "new_window": True,
        },
    ],
}


JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "sidebar_nav_small_text": False,
    "sidebar_disable_options": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}


# ============================================================
# DATABASE
# ============================================================

"""
Production:
    Render PostgreSQL URL will be stored in DATABASE_URL.

Local development:
    If DATABASE_URL does not exist, Django will use MySQL.

IMPORTANT:
Do NOT put production database passwords inside this file.
"""

DATABASE_URL = os.environ.get("DATABASE_URL")


if DATABASE_URL:

    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=not DEBUG,
        )
    }

else:

    # Local development database
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get(
                "MYSQL_DATABASE",
                "sps_solutions",
            ),
            "USER": os.environ.get(
                "MYSQL_USER",
                "root",
            ),
            "PASSWORD": os.environ.get(
                "MYSQL_PASSWORD",
                "123456",
            ),
            "HOST": os.environ.get(
                "MYSQL_HOST",
                "localhost",
            ),
            "PORT": os.environ.get(
                "MYSQL_PORT",
                "3306",
            ),
        }
    }

    # PyMySQL support for local MySQL
    try:
        import pymysql

        pymysql.install_as_MySQLdb()

    except ImportError:
        pass


# ============================================================
# PASSWORD VALIDATION
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME":
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator",
    },
    {
        "NAME":
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator",
    },
]


# ============================================================
# INTERNATIONALIZATION
# ============================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"


# WhiteNoise compressed static files
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },

    "staticfiles": {
        "BACKEND":
            "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# ============================================================
# MEDIA FILES
# ============================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# ============================================================
# DEFAULT PRIMARY KEY
# ============================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ============================================================
# PRODUCTION SECURITY
# ============================================================

if not DEBUG:

    # HTTPS
    SECURE_SSL_REDIRECT = True

    # Secure cookies
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # HTTP Strict Transport Security
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # Browser security
    SECURE_CONTENT_TYPE_NOSNIFF = True

    # Referrer policy
    SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

    # XSS protection
    SECURE_BROWSER_XSS_FILTER = True

    # Clickjacking protection
    X_FRAME_OPTIONS = "DENY"


# ============================================================
# DEVELOPMENT SECURITY
# ============================================================

else:

    SECURE_SSL_REDIRECT = False


# ============================================================
# EMAIL CONFIGURATION
# ============================================================

"""
Production email settings can be added later using Render
Environment Variables.

Example:

EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL
"""

EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND",
    "django.core.mail.backends.smtp.EmailBackend",
)

EMAIL_HOST = os.environ.get(
    "EMAIL_HOST",
    "",
)

EMAIL_PORT = int(
    os.environ.get(
        "EMAIL_PORT",
        "587",
    )
)

EMAIL_USE_TLS = (
    os.environ.get(
        "EMAIL_USE_TLS",
        "True",
    ).lower()
    == "true"
)

EMAIL_HOST_USER = os.environ.get(
    "EMAIL_HOST_USER",
    "",
)

EMAIL_HOST_PASSWORD = os.environ.get(
    "EMAIL_HOST_PASSWORD",
    "",
)

DEFAULT_FROM_EMAIL = os.environ.get(
    "DEFAULT_FROM_EMAIL",
    EMAIL_HOST_USER,
)


# ============================================================
# END OF SETTINGS
# ============================================================