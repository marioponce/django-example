from .base import *

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# If we are using postgresql

# If we are using sqlite3

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "example_db.sqlite3",
        "USER": "",    # Not used with sqlite3
        "PASSWORD": "",# Not used with sqlite3
        "HOST": "",    # Set to empty string for localhost. Not used with sqlite3
        "PORT": "",    # Set to empty string for default. Not used with sqlite3
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
