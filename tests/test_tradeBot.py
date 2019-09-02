import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import tradeBot
import settings
from modules import sanitize


class Test_TradeBot(unittest.TestCase):


    def test_settings(self):
        self.settings = settings.Settings()
        self.assertIsInstance(self.settings, object)

    def test_import_history(self):
        self.test_case = tradeBot.TradeBot()
        csv_file = 'M5_test_EURUSD.csv'
        self.assertRaises(Exception, self.test_case.import_history(csv_file))

    def test_analyze_history(self):
        self.test_case = tradeBot.TradeBot()
        self.assertRaises(Exception, self.test_case.analyze_history('EURUSD'))
    
    def test_get_external_data(self):
        import json
        self.test_case = tradeBot.TradeBot()
        data_dump = self.test_case.get_external_data('EURUSD')
        test_file = ('dumps/oanda_data_dump.json')
        with open (test_file, 'w') as file:
            json.dump(data_dump.json(), file)
            file.close() 
        data = data_dump.json()
        self.sanitized = sanitize.Sanitize(data)
        self.assertNotEqual(data_dump, 0)

if __name__ == '__main__':
    unittest.main()
