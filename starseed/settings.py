import os
import dj_database_url
from django.http import Http404

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

try:
    from getpass import getuser
    import pwd
except ImportError:
    def getuser():
        return os.environ.get('USERNAME', os.environ.get('USER'))
USER = getuser()


SECRET_KEY = '(1-b75%)a(!wb)ge(htjd9&8lzs1$@f-4+$dmvrj!^4hbfapwr'

DEBUG = True

TEMPLATE_DEBUG = True

SERVER_EMAIL = os.environ.get('SERVER_EMAIL')

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


INSTALLED_APPS = (
    'django.contrib.admin', # https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
    'django.contrib.sites', 
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'starseed',
    'taggit',
    'captcha',

)


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'starseed.urls'

WSGI_APPLICATION = 'starseed.wsgi.application'


SITE_ID = 1


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {    
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'starseeddb', 
            'USER': os.environ.get('PG_USER', 'starseed'),  
            'PASSWORD': os.environ.get('PG_PASSWORD', '$fmgd&*%SJ@SKJFR(@'),   
            'CONN_MAX_AGE': 600,
        }
    }

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025

if 'DATABASE_URL' in os.environ:
    DEBUG = False
    DATABASES['default'] = dj_database_url.config()
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    ROLLBAR = {
        'access_token': '8d17c8a107e347d2a50dac1e8ca5b618',
        'environment': 'development' if DEBUG else 'production',
        'root': BASE_DIR,
        'exception_level_filters': [
            (Http404, 'warning')
        ]
    }
    import rollbar
    rollbar.init(**ROLLBAR)
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME','blank')
    EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD','blank')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True



LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_URL = '/static/'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

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
            ],
        },
    },
]


# BOOTSTRAP3 = {
#     'jquery_url': '//code.jquery.com/jquery.min.js',
#     'css_url': None,
#     'theme_url': None,
#     'javascript_url': None,
#     'javascript_in_head': False,
#     'include_jquery': True,
#     'horizontal_label_class': 'col-md-3',
#     'horizontal_field_class': 'col-md-9',
#     'set_required': True,
#     'set_disabled': False,
#     'set_placeholder': True,
#     'required_css_class': '',
#     'error_css_class': 'has-error',
#     'success_css_class': 'has-success',
#     'formset_renderers':{
#         'default': 'bootstrap3.renderers.FormsetRenderer',
#     },
#     'form_renderers': {
#         'default': 'bootstrap3.renderers.FormRenderer',
#     },
#     'field_renderers': {
#         'default': 'bootstrap3.renderers.FieldRenderer',
#         'inline': 'bootstrap3.renderers.InlineFieldRenderer',
#     },
# }