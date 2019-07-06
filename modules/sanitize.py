class Sanitize():
    """
        Data should be in the following format
        DATE, TIME, OPEN, HIGH, LOW, CLOSE, VOLUME
        Lets not trust our data
    """
    def __init__(self, data):
        self.data = self.analyze(data)

    def input(self, data):
        try:
            self.analyze(data)
        except Exception as e:
            raise e
        return
    
    def findDateTime(self, row):
        try:
            date = row[0].split('.')
            date.append(row[1])
            return date
        except:
            raise KeyError
        return
    
    def analyze(self, data):
        import csv
        import re
        import time
        text_input = re.compile("^([A-Z])")
        file = open(data, 'r')
        file = csv.reader(file, delimiter=',')
        ncol=len(next(file)) # Read first line and count columns
        with open(data, newline='') as csvfile:
            input = csv.reader(csvfile, delimiter=',')
            cleaned = []
            i = 0
            for row in input:
                i = i + 1
                # Check for header
                if text_input.match(row[0]):
                    pass
                else:
                    # Work on input data here
                    _dateTime = self.findDateTime(row)
                    ## TODO fix row indexes to be in sync
                    _open = row[2]
                    _high = row[3]
                    _low = row[4]
                    _close = row[5]
                    _volume = row[6]
                    datetime = _dateTime[0]+'-'+_dateTime[1]+'-'+_dateTime[2]+'.'+_dateTime[3]
                    key = time.mktime(time.strptime(datetime, "%Y-%m-%d.%H:%M"))
                    cleaned.append([key, _open, _high, _low, _close, _volume])
            return cleaned
        raise FileNotFoundError