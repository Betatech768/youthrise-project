from decouple import config
import dj_database_url
from pathlib import Path
import os

# ---------------------------------------------
# BASE CONFIG
# ---------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="").split(",")

# Expire session when browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 3600  # 1 hour

# ---------------------------------------------
# APPLICATIONS
# ---------------------------------------------
INSTALLED_APPS = [
    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Your apps
    'blogpost',
    'exhibition',
    'galleries',
    'registration_app',
    'signin',
    'speakers',
    'sponsorship',
    'main',
    'admin',
    'Images',
    'Newsletter',
    'Contact_Us',

    # Third-party apps
    "storages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # for local compression
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

X_FRAME_OPTIONS = 'SAMEORIGIN'
XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']

ROOT_URLCONF = 'youthrise.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'youthrise.wsgi.application'

# ---------------------------------------------
# DATABASE
# ---------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wearepeopleconference',
        'USER': 'wearepeopleconference_user',
        'PASSWORD': '2zCWMAPsAVBltTOE2geXYXkVg8lBaH6Y',
        'HOST': 'dpg-d3afjf24d50c73d8ajs0-a.oregon-postgres.render.com',
        'PORT': '5432',
    }
}

# ---------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ---------------------------------------------
# INTERNATIONALIZATION
# ---------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------------------------
# CLOUD FLARE R2 CONFIG
# ---------------------------------------------
CLOUDFLARE_R2_BUCKET = config("CLOUDFLARE_R2_BUCKET")
CLOUDFLARE_R2_ACCESS = config("CLOUDFLARE_R2_ACCESS")
CLOUDFLARE_R2_SECRET = config("CLOUDFLARE_R2_SECRET")
CLOUDFLARE_R2_BUCKET_ENDPOINT = config("CLOUDFLARE_R2_BUCKET_ENDPOINT")

CLOUDFLARE_R2_CONFIG_OPTIONS = {
    "bucket_name": CLOUDFLARE_R2_BUCKET,
    "access_key": CLOUDFLARE_R2_ACCESS,
    "secret_key": CLOUDFLARE_R2_SECRET,
    "endpoint_url": CLOUDFLARE_R2_BUCKET_ENDPOINT,
    "default_acl": "public-read",
}

# ---------------------------------------------
# STATIC & MEDIA FILES
# ---------------------------------------------
if DEBUG:
    # Local development
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

else:
    # Production - use Cloudflare R2
    DEFAULT_FILE_STORAGE = "youthrise.storages_backends.MediaRootS3BotoStorage"
    MEDIA_URL = f"{CLOUDFLARE_R2_BUCKET_ENDPOINT}media/"

    STATICFILES_STORAGE = "youthrise.storages_backends.StaticFileStorage"
    STATIC_URL = f"{CLOUDFLARE_R2_BUCKET_ENDPOINT}static/"

# ---------------------------------------------
# DEFAULT AUTO FIELD
# ---------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
