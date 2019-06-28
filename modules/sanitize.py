class Sanitize():
    """
        Data should be in the following format
        DATE, TIME, OPEN, HIGH, LOW, CLOSE, VOLUME
        Lets not trust our data
    """
    def __init__(self, data):
        self.data = self.input(data)
        return

    def input(self, data):
        try:
            # Is input a file?
            self.analyze(data)
        except Exception as e:
            # Nope it wasnt a file
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
        raise FileNotFoundError