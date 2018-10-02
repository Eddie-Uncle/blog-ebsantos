#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Edson Santos'
SITENAME = 'Edson Bernardo Santos'
SITEURL = 'http://www.ebsantos.com'
SITETITLE = AUTHOR
SITELOGO = 'https://s.gravatar.com/avatar/c576edba5d85275fc58f4c183c8d9ad5?s=80'
MAIN_MENU = True
ROBOTS = 'index, follow'
PATH = 'content'

THEME = 'pelican-themes/Flex'
PLUGIN_PATHS =['pelican-plugins']
PLUGINS = ['neighbors','jinja2content','gzip_cache','i18n_subsites']

JINJA_ENVIRONMENT = {'extensions':['jinja2.ext.i18n','jinja2.ext.autoescape','jinja2.ext.with_']}

TIMEZONE = 'America/Costa_Rica'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', 'http://www.ebsantos.com/EdsonSantos.html'), 
       
         ('Kubernetes', 'http://kubernetes.io/'),
         ('Python', 'http://python.org/'),
         ('Oracle WebLogic', 'https://blogs.oracle.com/weblogicserver/')        )

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/bernardsp/'),
          ('github', 'https://github.com/Eddie-Uncle'),('twitter', 'https://twitter.com/bernardsp'),
          ('medium', 'https://medium.com/@edsonsantos_4197'))

MENUITEMS = (('Archives', '/archives.html'),('Categories', '/categories.html'),('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
