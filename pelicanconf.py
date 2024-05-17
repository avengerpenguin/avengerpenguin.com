from collections import defaultdict
from pathlib import Path
from typing import Any, Dict

from voltaire.pelican import *  # isort: skip

SITENAME = "Ross Fenning's Digital Garden"
PATH = "./Garden"
PAGE_PATHS = [""]
ARTICLE_PATHS = ["articles"]
ARTICLE_EXCLUDES = [".ipynb_checkpoints"]
PAGE_EXCLUDES = ARTICLE_PATHS + ARTICLE_EXCLUDES
FILENAME_METADATA = "(?P<title>.*)"

if "PLUGINS" not in globals():
    PLUGINS = []
PLUGINS += ["voltaire.search"]
TEMPLATE_PAGES = {
    "search.html": "search/index.html",
}

STATIC_PATHS = ["../extra"]
EXTRA_PATH_METADATA = {
    "../extra/CNAME": {"path": "CNAME"},
    "../extra/radar.json": {"path": "radar.json"},
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

MENUITEMS_START = (
    ("Home", "/"),
    ("Blog", "/blog/"),
    ("Search", "/search/"),
)

INDEX_SAVE_AS = "blog/index.html"

WEBASSETS_CONFIG = [
    ("SASS_LOAD_PATHS", [str(Path.cwd() / "node_modules")]),
    ("SASS_BIN", str(Path.cwd() / "node_modules" / ".bin" / "sass")),
    ("SASS_USE_SCSS", True),
]
DISQUS_SITE = "avengerpenguin"

if "MARKDOWN" not in globals():
    MARKDOWN: Dict[str, Dict[str, Any]] = defaultdict(dict)
    MARKDOWN["extension_configs"]["markdown.extensions.codehilite"] = {
        "css_class": "highlight"
    }

TYPOGRIFY = False
