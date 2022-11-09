from pathlib import Path

from voltaire.pelican import *

SITENAME = "Ross Fenning's Digital Garden"
PATH = "./Garden"
PAGE_PATHS = [""]
ARTICLE_PATHS = ["articles"]
PAGE_EXCLUDES = ARTICLE_PATHS
FILENAME_METADATA = "(?P<title>.*)"


# PLUGINS += [
#     'plugins.sitemap',
#     'plugins.pelican-open_graph',
#     'plugins.pelican-ipynb.markup',
# ]


PLUGINS += ["voltaire.search"]
TEMPLATE_PAGES = {
    "search.html": "search/index.html",
}

STATIC_PATHS = ["../extra"]
EXTRA_PATH_METADATA = {
    "../extra/CNAME": {"path": "CNAME"},
    "../extra/android-chrome-144x144.png": {"path": "android-chrome-144x144.png"},
    "../extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "../extra/browserconfig.xml": {"path": "browserconfig.xml"},
    "../extra/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "../extra/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "../extra/favicon.ico": {"path": "favicon.ico"},
    "../extra/mstile-150x150.png": {"path": "mstile-150x150.png"},
    "../extra/safari-pinned-tab.svg": {"path": "safari-pinned-tab.svg"},
    "../extra/site.webmanifest": {"path": "site.webmanifest"},
}

THEME_STATIC_PATHS += [Path.cwd() / "node_modules"]

MENUITEMS_START = (
    ("Home", "/"),
    ("Blog", "/blog/"),
    ("Search", "/search/"),
)

INDEX_SAVE_AS = "blog/index.html"

WEBASSETS_CONFIG = [("PYSCSS_LOAD_PATHS", [str(Path.cwd() / "node_modules")])]

# AUTHOR = 'Ross Fenning'
# SITENAME = 'Avenger Penguin'
# SITEURL = ''
#
# PATH = 'content'
# MARKUP = ('md', 'ipynb')
# IGNORE_FILES = ['.ipynb_checkpoints']
#
# IPYNB_EXTEND_STOP_SUMMARY_TAGS = [('h2', None), ('h3', None)]
#
# TIMEZONE = 'Europe/London'
#
# DEFAULT_LANG = 'en'
#
# # Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
#
# DEFAULT_PAGINATION = 10
#
# # Uncomment following line if you want document-relative URLs when developing
# #RELATIVE_URLS = True
#
# THEME = './theme'
#
# PAGE_URL = '{slug}'
# PAGE_SAVE_AS = '{slug}/index.html'
#
# CATEGORY_URL = '{slug}/'
# CATEGORY_SAVE_AS = '{slug}/index.html'
#
# MENUITEMS = (
#     ('Home', '/'),
# )
# DISPLAY_PAGES_ON_MENU = False
# DISPLAY_CATEGORIES_ON_MENU = True
# USE_FOLDER_AS_CATEGORY = True
#
# PLUGINS = [
#     'plugins.assets',
#     'plugins.summary',
#     'plugins.tag_cloud',
#     'plugins.sitemap',
#     'plugins.pelican-open_graph',
#     'plugins.pelican-ipynb.markup',
# ]
#
# SITEMAP = {
#     'format': 'xml',
#     'priorities': {
#         'articles': 0.5,
#         'indexes': 0.5,
#         'pages': 0.5
#     },
#     'changefreqs': {
#         'articles': 'monthly',
#         'indexes': 'daily',
#         'pages': 'monthly'
#     }
# }
#
#
# TYPOGRIFY = True
#
#
# STATIC_PATHS = ['extra/CNAME']
# EXTRA_PATH_METADATA = {
#     'extra/CNAME': {'path': 'CNAME'},
#     }
