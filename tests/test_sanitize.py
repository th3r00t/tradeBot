import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules import sanitize

class Test_Sanitize(unittest.TestCase):

    def test_csvfile(self):
        test_case = sanitize
        csv_file = 'dumps/M5_test_EURUSD.csv'
        self.assertRaises(Exception, test_case.Sanitize(csv_file))


if __name__ == '__main__':
    unittest.main()
