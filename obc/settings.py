import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w6$#oge2m8t!-=$b3!1cfqu74qv%%^jlccb)w8_nwaut=i9_(!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.2.109', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'haystack',
    'rest_framework',
    'crispy_forms',
    "verify_email.apps.VerifyEmailConfig",
    #moje apki
    'Home',
    'Api',
    'Accounts',
    'contact',
    'Obcpress',
    'Lists',
    'postman',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'obc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Home.context_processors.ile',
                'Home.context_processors.aktufoto',
                'Home.context_processors.contactmeview',
                'contact.context_processors.contact',
                'contact.context_processors.add_or_change_contact',
            ],
        },
    },
]

WSGI_APPLICATION = 'obc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pl'
LANGUAGES = [
    ('pl','Polish')

]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


CRISPY_TEMPLATE_PACK = 'bootstrap4'


EMAIL_BACKED = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.privateemail.com'
EMAIL_PORT = 587
EMAIL_USER_TLS = True
EMAIL_HOST_USER = 'admin@obrotni.de'
EMAIL_HOST_PASSWORD = 'klopik007'
DEFAULT_FROM_EMAIL = 'admin@obrotni.de'
EMAIL_USE_TLS = True
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#Alllauth
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
SITE_ID = 1
WHOOSH_INDEX = os.path.join(BASE_DIR, 'whoosh/')
ACCOUNT_EMAIL_VERIFICATION = 'none'

LOGIN_REDIRECT_URL = 'home'

HAYSTACK_CONNECTIONS = {
              'default': {
                    'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
                    'PATH': WHOOSH_INDEX
              }
    }

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_DOCUMENT_FIELD = 'text'

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'profil'
LOGOUT_REDIRECT_URL = 'homepage'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS =1
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Obrotni Biało-Czerwoni '


MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

POSTMAN_I18N_URLS = True  # default is False
POSTMAN_DISALLOW_ANONYMOUS = True  # default is False
POSTMAN_DISALLOW_MULTIRECIPIENTS = True  # default is False
POSTMAN_DISALLOW_COPIES_ON_REPLY = True  # default is False
POSTMAN_DISABLE_USER_EMAILING = True  # default is False
POSTMAN_FROM_EMAIL = 'admin@obrotni.de'  # default is DEFAULT_FROM_EMAIL

POSTMAN_AUTO_MODERATE_AS = True  # default is None
POSTMAN_SHOW_USER_AS = 'get_full_name'  # default is None
POSTMAN_NAME_USER_AS = 'username'  # default is None
POSTMAN_QUICKREPLY_QUOTE_BODY = True  # default is False
POSTMAN_NOTIFIER_APP = None  # default is 'notification'
POSTMAN_MAILER_APP = None  # default is 'mailer'
