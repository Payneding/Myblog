#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"Payne"
SITENAME = u"Paradise\x08 \x08\x08\x08"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Django', 'https://www.djangoproject.com/'),
         ('Python', 'https://docs.python.org/2/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (
         ('Myweibo', 'http://weibo.com/u/1933676623/'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME="new-bootstrap2"
#to control whether all those pages in pages directory  are displayed in the primary navigation menu(Default is True)
DISPLAY_PAGES_ON_MENU  = True
REVERSE_CATEGORY_ORDER = True
STATIC_PATHS = ['images', ]
