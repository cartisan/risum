from connection import *
import unittest


class TestConnection(unittest.TestCase):

    def test_connection_not_empty(self):
        self.assertTrue(Connection.connect())

if __name__ == '__main__':
    try: unittest.main()
    except SystemExit: pass
