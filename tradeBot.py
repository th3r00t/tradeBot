from modules import storage, sanitize
import os


class TradeBot():

    def __init__(self):
        self.storage = storage
        self.sanitize = sanitize

    def import_history(self, data):
        import re
        data = "dumps/%s"%(data)
        pattern = re.compile(r"[\w*]\.[\w\w\w]")
        datasplit = data.split('_')
        for string in datasplit:
            pair = re.search(pattern, string)
            if pair:
                pair = string.split('.')[0]
            else:
                pass
        if os.path.isfile(data):
            try:
                cleaned_data = self.sanitize.Sanitize(data)
                self.storage.Database().insert_history(cleaned_data.data, pair)
            except Exception as e:
                raise e
        else:
            print('Invalid File Specified')
            raise FileNotFoundError

    def analyze_history(self, pair):
        try:
            pass
        except Exception as e:
            raise e

    def prepare_report(self, pair):
        try:
            pass
        except Exception as e:
            raise e
