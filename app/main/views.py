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
