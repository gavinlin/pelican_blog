#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gavin Lin'
SITENAME = u"Gavin's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

TAGS_URL = 'tags.html'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('onelong', 'http://ways2u.com/'),
         ('zita', 'http://blog.csdn.net/ttxgz'),)

# Social widget
SOCIAL = (('github', 'https://github.com/gavinlin'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "blueidea"
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['latex', 'sitemap', 'multi_part']


DISPLAY_CATEGORIES_ON_SUBMENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_BASE_PAGES = True

#sitemap
SITEMAP = {
    'format':'xml',
    'priorities':{
        'articles':0.7,
        'indexes':0.6,
        'pages':0.5
    },
    'changefreqs':{
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

STATIC_PATHS = [
    u'CNAME',
    u'images',
    ]
