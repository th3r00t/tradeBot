import sqlite3
import time


class Database():
    """ 
    TradeBots database storage system
    """
    def __init__(self):
        # Connect to main database file,
        # and set a cursor for operations
        self.connection = sqlite3.connect('storage/neuralnet.db')
        self.c = self.connection.cursor()
    
    def check_for_table(self, table):
        # Check for the existance of the table
        return self.c.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name=%s'''%(table))

    def insert_history(self, data, table, timeframe):
        self.c.execute('''CREATE TABLE IF NOT EXISTS %s (timestamp, timeframe, open, high, low, close, volume, timeofinsert)'''%(table))
        for row in data:
            now = time.time()
            check_for_row = self.c.execute("SELECT timeframe FROM %s WHERE timestamp=%s" % (table, row[0]))
            row_exists = check_for_row.fetchone()
            if row_exists is None:
                self.c.execute('''INSERT INTO %s VALUES (%s, "%s", %s, %s, %s, %s, %s, %s)'''%(
                    table, row[0], timeframe, row[1], row[2], row[3], row[4], row[5], now
                ))    
        self.connection.commit()
        self.disconnect()
    
    def disconnect(self):
        self.c.close()
