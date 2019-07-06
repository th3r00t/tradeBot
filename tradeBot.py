from modules import storage, sanitize
import os
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import sqlite3
import sys
import requests

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TradeBot():
    """ Main Program Class """
    def __init__(self):
        self.storage = storage.Database
        self.sanitize = sanitize

    def import_history(self, data):
        """
        @param data: Name of file to pull history from
        """
        import re
        pair_pattern = re.compile(r"[\w*]\.[\w\w\w]")
        time_pattern = re.compile(r"^[a-zA-Z]*[0-9]$")
        datasplit = data.split('_')

        for string in datasplit:
            pair = re.search(pair_pattern, string)
            timeframe = re.match(time_pattern, string)
            if timeframe:
                self.timeframe = string
            if pair:
                pair = string.split('.')[0]
            else:
                pass

        data = "dumps/%s"%(data)
        if os.path.isfile(data):
            try:
                cleaned_data = self.sanitize.Sanitize(data)
                self.storage().insert_history(cleaned_data.data, pair, self.timeframe)
            except Exception as e:
                raise e
        else:
            print('Invalid File Specified')
            raise FileNotFoundError

    def analyze_history(self, pair):
        try:
            # con = 'storage/neuralnet.db'
            conn = self.storage()
            df = pd.read_sql("SELECT * FROM %s"%(pair), conn.connection, parse_dates='timestamp', index_col='timestamp')
            df['open'].plot()
            df['high'].plot()
            df['low'].plot()
            df['close'].plot()
            plt.show()
        except Exception as e:
            raise e
    
    def get_external_data(self, pair):
        # Get candlestick data from Oanda
        # Make sure pair variable is properly formatted "EUR_USD"
        import re
        delimeter = re.search('_', pair)
        if delimeter is None:
            pair = pair[:3]+"_"+pair[3:]
        payload = {
            "granularity":"S5",
            # "from":"",
            # "to":""
        }
        token = '00a07a87ae0cfd7313343971e50bbb19-83fc949e052da75e40a2d3f18475fe98'
        r=requests.get('https://api-fxpractice.oanda.com/v3/instruments/%s/candles'%(pair), 
                       headers={"Authorization":"Bearer %s"%(token)},
                       params=payload
                      )
        import pprint
        pprint.pprint(r.json())
        
    def prepare_report(self, pair):
        try:
            pass
        except Exception as e:
            raise e
