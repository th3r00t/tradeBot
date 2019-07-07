
#%%
import sys
import os

#%% [markdown]
# Now were going to set up a csv file and begin sanitizing it

#%%
csv_file = 'dumps/M5_hist_EURUSD.csv'

#%% [markdown]
# And set up our analysis system

#%%
def findDateTime(row):
    import re
    y = re.compile("[0-9]{4,4}")
    m = re.compile("[01-12]{2,2}")
    d = re.compile("[01-31]{2,2}")
    i = 0
    if y.match(row[0]):
        year = y.match(row[0])
        month = m.match(row[0])
        day = d.match(row[0])
        print("Match Found %s/%s/%s"%(year, month, day))
    else:
        print('No Match')
    return
            
            


#%%
def analyze(self, data):
    import csv
    import re
    text_input = re.compile("^([A-Z])")
    file = open(data, 'r')
    file = csv.reader(file, delimiter=',')
    ncol=len(next(file)) # Read first line and count columns
    with open(data, newline='') as csvfile:
        input = csv.reader(csvfile, delimiter=',')
        for row in input:
            # Check for header
            if text_input.match(row[0]):
                pass
            else:
                # Work on input data here
                _dateTime = self.findDateTime(row)
                _open = row[2]
                _high = row[3]
                _low = row[3]
                _close = row[4]
                _volume = row[5]
        return


#%%
import pandas as pd
from modules import storage
import sqlite3

def analyze_history(pair):
    con = sqlite3.connect('storage/neuralnet.db')
    df = pd.read_sql("SELECT * FROM %s"%(pair), con, parse_dates='timestamp', index_col='timestamp')
    df['open'].plot()
    df['high'].plot()
    df['low'].plot()
    df['close'].plot()


#%%
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.print_figure_kwargs = {'bbox_inches':None}")


#%%
analyze_history('EURUSD')


#%%
import pandas_datareader as pdr

df = pdr.av.forex.AVForexReader(symbols='EUR/USD', api_key='U8HB1I2CAKK8E3NO')
df.read()

#%% [markdown]
# Oanda Request for getting candle information

#%%
import requests
import pandas as pd
import json
from mpl_finance import candlestick_ohlc


payload = {
    "granularity":"S5",
    "price":"MBA",
    # "from":"",
    # "to":""
}
token = '00a07a87ae0cfd7313343971e50bbb19-83fc949e052da75e40a2d3f18475fe98'
r=requests.get('https://api-fxpractice.oanda.com/v3/instruments/EUR_USD/candles', 
               headers={"Authorization":"Bearer %s"%(token)},
               params=payload
              )
import pprint

data = json.dumps(r.json()['candles'])
df = pd.read_json(data, orient='records', typ='frame')
df.head()
df.plot()

pprint.pprint(df.head())




#%%
