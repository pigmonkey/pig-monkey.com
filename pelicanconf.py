#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Time
TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_DATE = 'fs'

# Blog settings
AUTHOR = u'Pig Monkey'
SITENAME = u'pig-monkey.com'
THEME = 'themes/vellum'
DEFAULT_LANG = u'en'
MENUITEMS = [('Blog', '/')]
DEFAULT_CATEGORY = 'general'

# Pagination
DEFAULT_PAGINATION = 6
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# URLs
SITEURL = 'http://localhost:8000'
FEED_DOMAIN = SITEURL
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
AUTHOR_SAVE_AS = ''

# Feeds
FEED_ATOM = 'feed'
CATEGORY_FEED_ATOM = 'category/%s/feed'
TAG_FEED_ATOM = 'tag/%s/feed'
FEED_MAX_ITEMS = DEFAULT_PAGINATION * 2

# Plugins
PLUGIN_PATHS = ['plugins',]
PLUGINS = ['tipue_search']

# Generation
PATH = 'content'
CSS_FILE = 'style.css'
USE_FOLDER_AS_CATEGORY = False
DIRECT_TEMPLATES = ('index', 'search')
STATIC_PATHS = ['media', '.htaccess', 'robots.txt']
SLUGIFY_SOURCE = 'basename'
TYPOGRIFY = True
