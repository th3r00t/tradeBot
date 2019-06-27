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
            self.analyse(data)
        except Exception as e:
            # Nope it wasnt a file
            raise e
        return

    def analyse(self, data):
        import csv
        import re
        import numpy as np
        text_input = re.compile("^([A-Z])")
        y = '[0-9]{4,4}'
        m = '[01-12]{2,2}'
        d = '[01-31]{2,2}'
        with open(data, newline='') as csvfile:
            input = csv.reader(csvfile, delimiter=',')
            for row in input:
                if text_input.match(row[0]):
                    pass
                else:
                    # Work on input data here
                    row,columns=row.shape()
            return
        raise FileNotFoundError