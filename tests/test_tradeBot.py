import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tradeBot


class Test_TradeBot(unittest.TestCase):
    
    def test_input_history(self):
        self.test_case = tradeBot.TradeBot()
        csv_file = 'M5_test_EURUSD.csv'
        self.assertRaises(Exception, self.test_case.import_history(csv_file))

    def test_analyze_history(self):
        self.test_case = tradeBot.TradeBot()
        self.assertRaises(Exception, self.test_case.analyze_history('EURUSD'))
    
    def test_get_external_data(self):
        self.test_case = tradeBot.TradeBot()
        self.assertRaises(Exception, self.test_case.get_external_data('EURUSD'))

if __name__ == '__main__':
    unittest.main()
