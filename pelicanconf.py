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
DEFAULT_PAGINATION = 8
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
FEED_ATOM = 'feed.atom'
CATEGORY_FEED_ATOM = 'category/{slug}/feed'
TAG_FEED_ATOM = 'tag/{slug}/feed'
FEED_MAX_ITEMS = DEFAULT_PAGINATION * 2

# Plugins
PLUGIN_PATHS = ['plugins',]
PLUGINS = ['tipue_search', 'tag_cloud']

# Generation
PATH = 'content'
CSS_FILE = 'style.css'
USE_FOLDER_AS_CATEGORY = False
DIRECT_TEMPLATES = ('index', 'search')
STATIC_PATHS = ['media', '.htaccess', 'robots.txt', 'key.asc', 'id.txt']
SLUGIFY_SOURCE = 'basename'
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.smarty': {},
    },
    'output_format': 'html5',
}
