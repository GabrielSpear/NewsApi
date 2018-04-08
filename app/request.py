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




def get_news(country,category):
    '''
    function of getting json response ro url
    '''
    get_news_url = base_url.format(country,category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_result = None


        if get_news_response['sources']:
            news_result_list = get_news_response['sources']
            news_result = process_results(news_result_list)

    return news_result

def process_results(news_list):
    '''
    function that takes in the movie results and transform them to a list
    '''
    news_result =[]

    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        print(id)
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')
