import os
import djcelery
import reusableapps
djcelery.setup_loader()

# Django settings for testsms project.
APPLICATION_DIR = os.path.dirname(globals()['__file__'])
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2','postgresql','mysql','sqlite3','oracle'
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': os.path.dirname(os.path.abspath(__file__)) + '/test.db',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost.
                                         # Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default.
                                         # Not used with sqlite3.
        'OPTIONS': {
           'init_command': 'SET storage_engine=INNODB',
        }
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(APPLICATION_DIR, 'resources')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = '/resources/'
MEDIA_URL = 'http://0.0.0.0:8000/resources/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/resources/admin/'
# Create symb link to admin directory
#ln -s /usr/local/lib/python2.6/dist-packages/django/contrib/admin/media/ admin

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ujau$^uei_ak=@-v8va(&@q_sc0^1nn*qpwyc-776n&qoam@+v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'common.filter_persist_middleware.FilterPersistMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'simu-sms.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(APPLICATION_DIR, 'templates'),
)
INTERNAL_IPS = ('127.0.0.1',)

REUSABLE_APPS_DIRS = (
'/usr/local/lib/python2.6/dist-packages/django-reusableapps/reusableapps',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.markup',
    'provider',
    'sms',
    'sms_billing',
    'sms_report',
    'api',
    'common',
    'djcelery',
    'django_extensions',
    'dateutil',
    #'debug_toolbar',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

INSTALLED_APPS = reusableapps.search(REUSABLE_APPS_DIRS, INSTALLED_APPS)

#LANGUAGES
#===========
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
    ('es', gettext('Spanish')),
    ('br', gettext('Brazilian')),
)

#IMPORT LOCAL SETTINGS
#=====================
try:
    from settings_local import *
except:
    pass
