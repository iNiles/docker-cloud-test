import unittest

import unh698


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = unh698.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        # Render the path
        rv = self.app.get('/')
        # search for phrase
        assert b'UNH698 Website' in rv.data
        
    def test_link_to_my_page(self):
        rv = self.app.get('/')  
        assert b'secondpage' in rv.data 

    def test_my_topic(self):
        rv = self.app.get('/secondpage')  
        assert b'poptart' in rv.data 


if __name__ == '__main__':
    unittest.main()
