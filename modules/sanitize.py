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
            date = [list(row)[0].split('T')[0], list(row)[0].split('T')[1][0:-1]]
            return date

        return

    def stream(self, data):
        """
        :param data:
        :return: Array of organized data _ask['o'],_ask['h'],_ask['l'],_ask['c']
        """
        clean = []
        for row in data['candles']:
            _date = row['time']
            _ask = row['ask']
            _bid = row['bid']
            _mid = row['mid']
            _vol = row['volume']
            # TODO arrange streamed data
            _row = {_date:{'ask':_ask,'mid':_mid,'bid':_bid},'vol':_vol}
            clean.append(_row)
        return clean

    def analyze(self, data):
        import csv
        import re
        import time
        text_input = re.compile("^([A-Z])")
        ## TODO Add try block to check whether incoming data is a file
        try:
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
                        _open = row[2]
                        _high = row[3]
                        _low = row[4]
                        _close = row[5]
                        _volume = row[6]
                        datetime = _dateTime[0]+'-'+_dateTime[1]+'-'+_dateTime[2]+'.'+_dateTime[3]
                        key = time.mktime(time.strptime(datetime, "%Y-%m-%d.%H:%M"))
                        cleaned.append([key, _open, _high, _low, _close, _volume])
                        #TODO Reformat for new storage system
                return cleaned
        except:
            data = self.stream(data)
            cleaned = []
            for row in data:
                _dateTime = self.findDateTime(row)
                key = list(row)[0]
                _ask_o = row[key]['ask']['o']
                _ask_h = row[key]['ask']['h']
                _ask_l = row[key]['ask']['l']
                _ask_c = row[key]['ask']['c']
                _bid_o = row[key]['bid']['o']
                _bid_h = row[key]['bid']['h']
                _bid_l = row[key]['bid']['l']
                _bid_c = row[key]['bid']['c']
                _mid_o = row[key]['mid']['o']
                _mid_h = row[key]['mid']['h']
                _mid_l = row[key]['mid']['l']
                _mid_c = row[key]['mid']['c']
                _volume = row['vol']
                key = time.mktime(time.strptime(_dateTime[0]+'.'+_dateTime[1].split('.')[0], "%Y-%m-%d.%H:%M:%S"))
                #TODO Format for storage
                cleaned.append([key, _open, _high, _low, _close, _volume])
            return cleaned