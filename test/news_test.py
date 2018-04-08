import unittest
from app.models import Articles

class NewsTest(unittest.TestCase):
    '''
    test behaviour of news class
    '''

    def setUp(self):
        '''
        will run before every test
        '''
        self.new_articles = Articles('id','name','author','title','description','url','urlToImage','publishedAt')
