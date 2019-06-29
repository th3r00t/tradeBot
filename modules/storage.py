import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect('storage/neuralnet.db')
        self.c = self.connection.cursor()
    
    def insert_history(self, data, pair):
        self.c.execute('''CREATE TABLE IF NOT EXISTS %s (timestamp, open, high, low, close, volume)'''%(pair))
        for row in data:
            self.c.execute('''INSERT INTO %s VALUES (%s, %s, %s, %s, %s, %s)'''%(
                pair, row[0], row[1], row[2], row[3], row[4], row[5]
            ))
        self.connection.commit()
        self.disconnect()
    
    def disconnect(self):
        self.c.close()
