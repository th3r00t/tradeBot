import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tradeBot


class Test_TradeBot(unittest.TestCase):

    def test_input_history(self):
        test_case = tradeBot.TradeBot()
        csv_file = 'M5_hist_EURUSD.csv'
        self.assertRaises(Exception, test_case.import_history(csv_file))


if __name__ == '__main__':
    unittest.main()
