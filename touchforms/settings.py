import django # for verison sniffing
import util

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',             # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'xformplayer.db',             # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

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
MEDIA_ROOT = 'data'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = ( 
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "touchforms.context_processors.meta",
    'django.core.context_processors.static' if django.VERSION >= (1, 3) else 'staticfiles.context_processors.static',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'touchforms.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.staticfiles' if django.VERSION >= (1, 3) else 'staticfiles',
    'formplayer'
)

#e.g., 1.0, 1.1a, 1.2b, 1.3rc2
#this should ONLY be set in a release/maintenance branch, NEVER in the dev branch!
RELEASE_VERSION = None

import os
ROOT_DIR = os.path.normpath(os.path.dirname(__file__))
STATIC_DOC_ROOT = os.path.join(ROOT_DIR, "formplayer", "static")
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, 'staticroot')
XFORMS_BOOTSTRAP_PATH = "static/demo_forms"
XFORMS_PATH = "data/xforms"
XFORMS_PLAYER_URL = "http://localhost:4444/"
OFFLINE_TOUCHFORMS_PORT = 4444
TOUCHFORMS_AUTOCOMPL_DATA_DIR = os.path.join(ROOT_DIR, 'static', 'census')

LOG_FILE = os.path.join(ROOT_DIR, 'touchforms.log')
init_logging = lambda: util.default_logging(LOG_FILE)

#### IMPORT LOCALSETTINGS ####
try:
    from localsettings import *
except ImportError:
    pass

TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS

util.initialize_logging(init_logging)

REVISION = util.get_revision('git', ROOT_DIR, 'flag')

GMAPS_API_KEY = ''
SECRET_KEY = 'you should really change this'
