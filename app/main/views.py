from flask import render_template
from . import main


#views


@main.route('/')
def index():
    '''
    function that returns index page
    '''
    message = 'hello world'
    title = 'One of the best News Website in the world'






    @main.route('/news/<id>')
def news(id):
    """
    View articles page that returns the news article from a highlight
    """
    news_args = get_details(id)
    highlight_args = 'Route Working!!'
    # name = f'{results_list}'
    return render_template('news.html',highlight_param=highlight_args,news=news_args)
