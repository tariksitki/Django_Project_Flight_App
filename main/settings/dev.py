
from .base import *

THIRD_PARTY_APPS = [
    "debug_toolbar",

]

INSTALLED_APPS += THIRD_PARTY_APPS


THIRD_PARTY_MIDDLEWARE = [
    #### debug / redoc:
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

MIDDLEWARE += THIRD_PARTY_MIDDLEWARE



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

## dev de sqlite, production da ise 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



### redoc / debug
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]