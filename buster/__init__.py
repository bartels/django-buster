"""
A Django app for appending cache buster strings to html resources, and loading
json file created with gulp-buster.
see: https://github.com/UltCombo/gulp-buster

Example use of the templatetag:
    <script src="{% buster %}{% static "js/app.js" %}{% endbuster %}"></script>
"""

import re
import json

from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings


# The file to read cache buster json from
BUSTER_FILE = getattr(settings, 'BUSTER_FILE', 'dist/busters.json')

# Whether to cache the buster json on first load
BUSTER_CACHE = getattr(settings, 'BUSTER_CACHE', not settings.DEBUG)

BUSTER_CACHE_KEY = 'buster_cache'
cache = {}


def get_buster_json(buster_file=BUSTER_FILE):
    """
    Returns json data either from cache or from the busters file from
    staticfiles storage.
    """
    # First check for cached version
    if BUSTER_CACHE:
        buster_json = cache.get(BUSTER_CACHE_KEY)
        if buster_json is not None:
            return buster_json

    # Look for busters file in staticfiles storage
    buster_json = ''
    if staticfiles_storage.exists(buster_file):
        with staticfiles_storage.open(buster_file) as file_:
            contents = file_.read()
            file_.flush()

        # Try to load the json from file
        try:
            buster_json = json.loads(contents)
        except ValueError:
            pass

    # cache the json
    cache[BUSTER_CACHE_KEY] = buster_json

    return buster_json


def get_buster_for_url(url, busters=None):
    """
    Returns the buster hash for the given url
    """
    # Get the busters json
    if busters is None:
        busters = get_buster_json()
    if not busters:
        return None

    # Cacluate the path relative to static root
    base_url = settings.STATIC_URL
    relpath = re.sub(r'^' + base_url, '', url).lstrip('/')

    # Try to return hash keyed by the path
    try:
        return busters[relpath]
    except KeyError:
        return None
