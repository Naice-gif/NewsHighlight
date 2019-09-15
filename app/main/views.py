from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source
from ..models import Source
from ..arts import Article


# Views
@main.route('/')
def index():  

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news sources
    entertainment_news = get_source('entertainment')
    politics_news = get_source('politics')
    animals_news = get_source('animals')
    title = 'Home - Welcome to your worldwide news source'
    return render_template('index.html', title = title, entertainment = entertainment_news, politics = politics_news, animals = animals_news )


@main.route('/news/<id>')
def source(id):
   '''
   function that returns articles by source id
   '''
   article_source = get_articles(id)
   title = f'{id}| Articles'
   return render_template('articles.html',title = title, articles = article_source)



