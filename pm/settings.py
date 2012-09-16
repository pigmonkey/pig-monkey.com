# Django settings for pm project.
import os
import sys

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Pig Monkey', 'pm@pig-monkey.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = False

SITE_ID = 1

PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(PROJECT_ROOT, 'pm')
APPS_DIR = os.path.join(PROJECT_ROOT, 'apps')
sys.path.append(APPS_DIR)
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'pm.urls'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(PROJECT_ROOT, 'cache')
    }
}

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.comments',
    'django_extensions',
    'base',
    'debug_toolbar',
    'compressor',
    'contact',
    'inlines',
    'simplesearch',
    'taggit',
    'taggit_templatetags',
    'django_markup',
    'disqus',
    'vellum',
    'sorl.thumbnail',
    'geartracker',
    'badgr',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'vellum.context_processors.blog_settings',
    'badgr.context_processors.flickr',
    'base.context_processors.github_activity',
)

INTERNAL_IPS = ('127.0.0.1',)

# Compressor Settings
COMPRESS_CSS_FILTERS = ['compressor.filters.cssmin.CSSMinFilter']

# Blog settings
BLOG_DESCRIPTION = "Here are recorded many goings and comings, doings and beings; stories, symbols and meanings."
BLOG_PAGESIZE = 8
BLOG_USEDISQUS = True
BLOG_SMARTYPANTS = True

# Disqus
DISQUS_WEBSITE_SHORTNAME = 'pigmonkey'

# Flickr Settings
FLICKR_USERID = '17680393@N03'
FLICKR_NUMPHOTOS = 15
FLICKR_IMAGESIZE = 'q'

# Mail Settings
DEFAULT_FROM_EMAIL = 'pm@pig-monkey.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Import development-specific settings.
try:
    from settings_dev import *
except ImportError:
    pass

# Import production-specific settings.
try:
    from settings_live import *
except ImportError:
    pass
