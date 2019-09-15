import urllib.request,json
from .models import Source
# from app import main

# Getting api key
api_key = None
# Getting the source base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    print('Hey')
    print(base_url)
    print(api_key)

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
           source_results_list = get_source_response['sources']
           source_results = process_results(source_results_list)


    return source_results


def process_results(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

      
        source_object = Source(id,name,description,url, category,language, country)
        source_results.append(source_object)

    return source_results


    

def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    print(id)
    print(apiKey)
    print(articles_url)
    get_articles_url = articles_url.format(id,apiKey)
    print(get_articles_url)


    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())
        articles_object = None

        if articles_results['articles']:
           articles_object = process_articles(articles_results['articles'])

    return articles_object



def process_articles(articles_list):
    '''
    '''
    articles_object = []

     
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        content = article_item.get('content')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')

        if image:
           articles_result = Article(id,title, description, image, date, author, url,content)
           articles_object.append(articles_result)

    return articles_object

