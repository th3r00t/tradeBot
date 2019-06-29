import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import settings

class Test_Settings(unittest.TestCase):

    def test_OpenSettings(self):
        test_case = settings.Settings()
        self.assertRaises(Exception, test_case.setup())


if __name__ == '__main__':
    unittest.main()
