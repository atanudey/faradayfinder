"""
Django settings for faradayfinder project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2d#pf-53yg0l(&9%bdu$=m+m^jve_#&+mb@6je)-x7ygpvka5j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'pagination',
    'custom_user',
    'contents',
    'emails',
    'logs',
    'jobs',
    'postman',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'faradayfinder.urls'

WSGI_APPLICATION = 'faradayfinder.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

'''
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'de273uhlk1d7la',
         'USER': 'lwgmueortgipts',
         'PASSWORD': 'tcQtRlyLw-n991CDbCgBuI1MmC',
         'HOST': 'ec2-107-20-148-211.compute-1.amazonaws.com', # '127.0.0.1' probably works also
         'PORT': '5432',
     }
}
'''

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'ff',
         'USER': 'root',
         'PASSWORD': 'FE-120',
         'HOST': 'localhost', # '127.0.0.1' probably works also
         'PORT': '5432',
     }
}

"""
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'ff',
         'USER': 'bhawani',
         'PASSWORD': '121212',
         'HOST': 'localhost', # '127.0.0.1' probably works also
         'PORT': '5432',
     }
}
"""


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'custom_user.CustomUser'

# defining template directory
TEMPLATE_DIRS = [os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')]

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-erase',
    '--cover-package=custom_user,utils,logs,emails,contents'
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(thread)d %(threadName)s %(asctime)s %(levelname)s %(filename)s %(name)s: %(message)s',
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logging.log',  # please change this accordingly
            'maxBytes': 1024 * 1024 * 500,
            'backupCount': 100,
            'formatter': 'standard',
        },
        'stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    '': {
        'handlers': ['default', 'stdout'],
        'level': 'DEBUG',
        'propagate': True
    },

    }
}

WEBSITE_TITLE = "FaradayFinder"
WEBSITE_URL = "http://faradayfinder.herokuapp.com"
SIGNUP_EMAIL = "zach@faradayfinder.com"
SUPPORT_EMAIL = "support@faradayfinder.com"

CURRENCY_LIST = {'ILS': 'Israeli New Sheqel', 'EUR': 'Euro', 'JPY': 'Japanese Yen', 'HKD': 'Hong Kong Dollar', 'CZK': 'Czech Koruna', 'TWD': 'Taiwan New Dollar', 'NZD': 'New Zealand Dollar', 'CHF': 'Swiss Franc', 'SEK': 'Swedish Krona', 'HUF': 'Hungarian Forint ', 'SGD': 'Singapore Dollar', 'DKK': 'Danish Krone', 'GBP': 'Pound Sterling', 'MYR': 'Malaysian Ringgit', 'CAD': 'Canadian Dollar', 'THB': 'Thai Baht', 'AUD': 'Australian Dollar', 'TRY': 'Turkish Lira', 'USD': 'U.S. Dollar', 'NOK': 'Norwegian Krone', 'MXN': 'Mexican Peso', 'PHP': 'Philippine Peso', 'PLN': 'Polish Zloty', 'BRL': 'Brazilian Real '}
CURRENCY_CHOICES = CURRENCY_LIST.items();

PAYMENT_GATEWAY_URL = "https://www.sandbox.paypal.com/cgi-bin/webscr"
PAYMENT_MERCHANT_EMAIL = "tanusree@xentrictechnologies.com"
PAYMENT_BUTTON = "PP-BuyNowBF"
PAYMENT_ITEM_NAME = "FaradayFinder Job Posting Payment"
PAYMENT_ITEM_NUMBER = "JOBPOSTING"
PAYMENT_AMOUNT = "20"
PAYMENT_TAX = "0"
PAYMENT_QUANTITY = "1"
PAYMENT_NO_NOTE = "1"
PAYMENT_CURRENCY_CODE = "USD"
PAYMENT_ADDRESS_OVERRIDE = "1"
PAYMENT_FIRST_NAME = "John"
PAYMENT_LAST_NAME = "Doe"
PAYMENT_ADDRESS1 = "345 Lark Ave"
PAYMENT_CITY = "San Jose"
PAYMENT_STATE = "CA"
PAYMENT_ZIP = "95121"
PAYMENT_COUNTRY = "US"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'book!@#123'
EMAIL_HOST_USER = 'c2c.book4sale@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# EMAIL_HOST = 'smtp.mail.yahoo.com'
# EMAIL_HOST_PASSWORD = 'bhanu0915'
# EMAIL_HOST_USER = 'bhawani021'
# EMAIL_PORT = 465
# EMAIL_USE_TLS = True

LOGIN_REDIRECT_URL = '/accounts/dashboard/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

POSTMAN_NAME_USER_AS = 'email'
POSTMAN_DISALLOW_ANONYMOUS = True  # default is False
#POSTMAN_DISALLOW_MULTIRECIPIENTS = True  # default is False
POSTMAN_DISALLOW_COPIES_ON_REPLY = False  # default is False
#POSTMAN_DISABLE_USER_EMAILING = True  # default is False
POSTMAN_AUTO_MODERATE_AS = True  # default is None
POSTMAN_SHOW_USER_AS = 'get_full_name'  # default is None
POSTMAN_QUICKREPLY_QUOTE_BODY = True  # default is False
POSTMAN_NOTIFIER_APP = None  # default is 'notification'
POSTMAN_MAILER_APP = None  # default is 'mailer'

#The default amount of items to show on a page if no number is specified.
PAGINATION_DEFAULT_PAGINATION = 10
#The number of items to the left and to the right of the current page to display (accounting for ellipses).
PAGINATION_DEFAULT_WINDOW = 3
#The minimum number of items allowed on the last page, defaults to zero.
PAGINATION_DEFAULT_ORPHANS = 0
#Determines whether an invalid page raises an Http404 or just sets the invalid_page context variable. True does the former and False does the latter.
#PAGINATION_INVALID_PAGE_RAISES_404 = True 

FIXTURE_DIRS = (
    'fixtures/data/',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
)