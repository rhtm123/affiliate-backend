from affiliateBackend.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
        'OPTIONS': {'sslmode': 'require'},
        }
}

ALLOWED_HOSTS = ['mastdeal.up.railway.app', 'mdh.thelearningsetu.com', "localhost"]


CORS_ALLOWED_ORIGINS = [
    'https://mastdeal.up.railway.app',
    "https://mdh.thelearningsetu.com",
    'https://www.mastdealhai.com'
]

# Disable these settings to ensure only allowed origins are permitted
CORS_ALLOW_CREDENTIALS = False  # Disable credentials for added security
CORS_ALLOW_ALL_ORIGINS = False  # Explicitly disallow all origins

CSRF_TRUSTED_ORIGINS = [
    'https://mastdeal.up.railway.app',
    "https://mdh.thelearningsetu.com",
    "https://www.mastdealhai.com",
]
CORS_ORIGIN_WHITELIST = [
    'https://mastdeal.up.railway.app',
    "https://mdh.thelearningsetu.com",
    "https://www.mastdealhai.com",
]