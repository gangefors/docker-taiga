from os import getenv as ge
from typing import Any

from .common import *


def getenv(env: str, default: Any) -> str:
    """Return env var if set and not empty, otherwise default.

       Also convert 'true'/'false' to bool values."""
    got_env = ge(env)
    got_env = False if got_env and got_env.lower() == "false" else got_env
    got_env = True if got_env and got_env.lower() == "true" else got_env
    return default if got_env is None or got_env == "" else got_env


#########################################
# GENERIC
#########################################

HOSTNAME = getenv("HOSTNAME", "localhost")

DEBUG = getenv("DEBUG", False)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': getenv("DB_NAME", "taiga"),
        'USER': getenv("DB_USER", "taiga"),
        'PASSWORD': getenv("DB_PASSWORD", "taiga"),
        'HOST': getenv("DB_HOST", "taiga-db"),
        'PORT': getenv("DB_PORT", "5432"),
    }
}

FRONT_SCHEME = getenv("FRONT_SCHEME", "https")
FRONT_DOMAIN = getenv("FRONT_DOMAIN", HOSTNAME + ":9001")
FRONT_URI = FRONT_SCHEME + FRONT_DOMAIN

SITES["api"]["scheme"] = getenv("API_SCHEME", "http")
SITES["api"]["domain"] = getenv("API_DOMAIN", HOSTNAME + ":8000")
SITES["front"]["scheme"] = FRONT_SCHEME
SITES["front"]["domain"] = FRONT_DOMAIN

TIME_ZONE = getenv("TIME_ZONE", "UTC")
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = getenv("LANGUAGE_CODE", "en-us")

# Static configuration.
MEDIA_ROOT = "/taiga/media"
STATIC_ROOT = "/taiga/static"

# The absolute url is mandatory because attachments
# urls depends on it. On production should be set
# something like https://media.taiga.io/
MEDIA_URL = FRONT_URI + "/media/"
STATIC_URL = FRONT_URI + "/static/"

ADMIN_MEDIA_PREFIX = STATIC_URL + "/admin/"

SECRET_KEY = getenv("SECRET_KEY", "secretkey")


#########################################
# MAIL SYSTEM SETTINGS
#########################################

DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL", "no-reply@" + HOSTNAME)
SERVER_EMAIL = getenv("SERVER_EMAIL", DEFAULT_FROM_EMAIL)
EMAIL_USE_TLS = getenv("EMAIL_USE_TLS", False)
EMAIL_HOST = getenv("EMAIL_HOST", HOSTNAME)
EMAIL_PORT = getenv("EMAIL_PORT", 25)
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD", "")


#########################################
# REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = getenv("PUBLIC_REGISTER_ENABLED", True)

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
USER_EMAIL_ALLOWED_DOMAINS = getenv("USER_EMAIL_ALLOWED_DOMAINS", "").split()


#########################################
# FEEDBACK
#########################################

# Note: See config in taiga-front too
FEEDBACK_ENABLED = getenv("FEEDBACK_ENABLED", False)
FEEDBACK_EMAIL = getenv("FEEDBACK_EMAIL", "support@taiga.io")
