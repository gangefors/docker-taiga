from os import getenv

from .common import *


#########################################
## GENERIC
#########################################

HOSTNAME = getenv("HOSTNAME", "localhost")

ADMINS = (
    (
        getenv("TAIGA_ADMIN", "Admin"),
        getenv("TAIGA_ADMIN_EMAIL", "admin@" + HOSTNAME)
    ),
)

DEBUG = getenv("DEBUG", False)
TEMPLATE_DEBUG = getenv("TEMPLATE_DEBUG", DEBUG)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': getenv("DB_NAME", "taiga"),
        'USER': getenv("DB_USER", "taiga"),
        'PASSWORD': getenv("DB_PASSWORD", "password"),
        'HOST': getenv("DB_HOST", "postgres"),
        'PORT': getenv("DB_PORT", "5432"),
    }
}

API_SCHEME = getenv("API_SCHEME", "http")
API_DOMAIN = getenv("API_DOMAIN", HOSTNAME + ":8000")
API_NAME = getenv("API_NAME", "api")
API_URI = API_SCHEME + API_DOMAIN

FRONT_SCHEME = getenv("FRONT_SCHEME", "http")
FRONT_DOMAIN = getenv("FRONT_DOMAIN", HOSTNAME + ":9001")
FRONT_NAME = getenv("FRONT_NAME", "front")
FRONT_URI = FRONT_SCHEME + FRONT_DOMAIN

SITES = {
   "api": {
      "scheme": API_SCHEME,
      "domain": API_DOMAIN,
      "name": API_NAME,
   },
   "front": {
      "scheme": FRONT_SCHEME,
      "domain": FRONT_DOMAIN,
      "name": FRONT_NAME,
   },
}

SITE_ID = API_NAME

TIME_ZONE = getenv("TIME_ZONE", "UTC")
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = getenv("LOCALE", 'en-us')

# Static configuration.
MEDIA_ROOT = "/taiga/media"
STATIC_ROOT = "/taiga/static"

# The absolute url is mandatory because attachments
# urls depends on it. On production should be set
# something like https://media.taiga.io/
MEDIA_URL = FRONT_URI + "/media/"
STATIC_URL = FRONT_URI + "/static/"

ADMIN_MEDIA_PREFIX = getenv("ADMIN_MEDIA_PREFIX", STATIC_URL + "/admin/")

SECRET_KEY = getenv("SECRET_KEY", "theveryultratopsecretkey")


#########################################
## THROTTLING
#########################################

#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon": "20/min",
#    "user": "200/min",
#    "import-mode": "20/sec",
#    "import-dump-mode": "1/minute"
#}


#########################################
## MAIL SYSTEM SETTINGS
#########################################

DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL", "no-reply@" + HOSTNAME)
SERVER_EMAIL = getenv("SERVER_EMAIL", DEFAULT_FROM_EMAIL)
#CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300  #seconds

# EMAIL SETTINGS EXAMPLE
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = getenv("EMAIL_USE_TLS", False)
EMAIL_HOST = getenv("EMAIL_HOST", HOSTNAME)
EMAIL_PORT = getenv("EMAIL_PORT", 25)
EMAIL_HOST_USER = getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = getenv("EMAIL_HOST_PASSWORD", "")

# GMAIL SETTINGS EXAMPLE
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'youremail@gmail.com'
#EMAIL_HOST_PASSWORD = 'yourpassword'


#########################################
## REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = getenv("PUBLIC_REGISTER_ENABLED", True)

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
#USER_EMAIL_ALLOWED_DOMAINS = None

# PUCLIC OR PRIVATE NUMBER OF PROJECT PER USER
#MAX_PRIVATE_PROJECTS_PER_USER = None  # None == no limit
#MAX_PUBLIC_PROJECTS_PER_USER = None  # None == no limit
#MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None  # None == no limit
#MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None  # None == no limit

# GITHUB SETTINGS
#GITHUB_URL = "https://github.com/"
#GITHUB_API_URL = "https://api.github.com/"
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"


#########################################
## SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
#FRONT_SITEMAP_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second


#########################################
## FEEDBACK
#########################################

# Note: See config in taiga-front too
FEEDBACK_ENABLED = getenv("FEEDBACK_ENABLED", True)
FEEDBACK_EMAIL = getenv("FEEDBACK_EMAIL", "support@taiga.io")


#########################################
## STATS
#########################################

STATS_ENABLED = getenv("STATS_ENABLED", False)


#########################################
## CELERY
#########################################

#from .celery import *
#CELERY_ENABLED = True
#
# To use celery in memory
#CELERY_ENABLED = True
#CELERY_ALWAYS_EAGER = True
