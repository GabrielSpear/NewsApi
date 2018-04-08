import urllib.request,json
from .models import Articles
from .models import Source
# Getting api key
api_key = None
# Getting the movie base url
base_url = None
#
source_url =None


def configure_request(app):
    global api_key,base_url,source_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_KEY_URL']
    source_url = app.config['NEWS_API_SOURCES_URL']
