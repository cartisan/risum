from connection import *
import unittest


class TestConnection(unittest.TestCase):

    def setUp(self):
        self.c = Connection()
    
    def test_connection_not_empty(self):
        self.c.connect()
        self.assertTrue(self.c.response_to_str())

    def test_get_city_dict(self):
        dict = self.c.get_city_dict()
        
        self.assertEqual(dict['Berlin'],30) 
        
if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
