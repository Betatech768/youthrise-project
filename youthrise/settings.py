
from decouple import config
import dj_database_url
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="").split(",")




# Expire session when browser is closed
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  

# Or set lifetime in seconds (e.g., 1 hour)
SESSION_COOKIE_AGE = 3600  


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
   'django.contrib.humanize',
   'Newsletter',
   'Contact_Us',
   "storages",

    ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ✅ add this line
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


X_FRAME_OPTIONS = 'SAMEORIGIN'

XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']

ROOT_URLCONF = 'youthrise.urls'

# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

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



# Cloudflare R2 credentials



# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'youthrise_project',
#         'USER': 'goodness',
#         'PASSWORD': 'chinexy',
#         'HOST': 'localhost',   # or the database server IP
#         'PORT': '3306',        # default MySQL port
#     }
# }


# DATABASES = {
#     'default': dj_database_url.parse(
#         config("DATABASE_URL"),
#         conn_max_age=600,  # keep connection alive
#         ssl_require=False
#     )
# }



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





# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]  # only if you have a /static folder

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Let WhiteNoise handle compressed static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


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

STORAGES = {
    "default": {
        "BACKEND": "youthrise.storages_backends.MediaRootS3BotoStorage",
        "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS,
    },
    "staticfiles": {
        "BACKEND": "youthrise.storages_backends.StaticFileStorage",
        "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS,
    },
}