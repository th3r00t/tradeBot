import mysql.connector
#import sqlite3
import time
import settings


class Database():
    """ 
    TradeBots database storage system
    """
    def __init__(self):

        """
        # Connect to main database file,
        # and set a cursor for operations
        self.connection = sqlite3.connect('storage/neuralnet.db')
        self.c = self.connection.cursor()
        """
        self.settings = settings.Settings().settings
        self.connection = mysql.connector.connect(**self.settings['sql_cfg'])
        self.c = self.connection.cursor()
        # Check for the existance of the table
        # return self.c.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name=%s'''%(table))

    def create_table(self, table):
        self.c.execute("CREATE TABLE IF NOT EXISTS %s ("
                       "time_stamp FLOAT(25),"
                       "time_frame FLOAT(25),"
                       "ask_open DECIMAL(7, 5),"
                       "ask_high DECIMAL(7, 5),"
                       "ask_low DECIMAL(7, 5),"
                       "ask_close DECIMAL(7, 5),"
                       "mid_open DECIMAL(7, 5)," 
                       "mid_high DECIMAL(7, 5)," 
                       "mid_low DECIMAL(7, 5),"  
                       "mid_close DECIMAL(7, 5),"
                       "bid_open DECIMAL(7, 5),"
                       "bid_high DECIMAL (7, 5),"
                       "bid_low DECIMAL (7, 5),"
                       "bid_close DECIMAL (7, 5),"
                       "volume FLOAT(8),"
                       "time_of_insert FLOAT(25))" % table)  # 16 columns

    def insert_history(self, data, table, time_frame):
        try:
            self.create_table(table)
        except:
            pass
        for row in data:
            now = time.time()
            try:
                check_for_row = self.c.execute("SELECT timeframe FROM %s WHERE timestamp=%s" % (table, row[0]))
                row_exists = check_for_row.fetchone()
            except AttributeError:
                row_exists = None
                pass
            if row_exists is None:
                self.c.execute('''INSERT INTO %s VALUES (%s,
                "%s",
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                "%s",
                %s,
                %s,
                %s,
                %s,
                %s,
                %s)''' % (
                    table,
                    row[0],
                    time_frame,
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    row[12],
                    row[13],
                    now
                ))
        self.connection.commit()
        self.disconnect()

    def disconnect(self):
        self.c.close()
