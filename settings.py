import os
import sys
import json

class Settings():

    def read_settings(self):
        return open('settings.json', 'r')

    def write_settings(self):
        return open('settings.json', 'w')

    def setup(self):
        settings_file = self.read_settings()
        settings = json.load(self.read_settings())
        settings_file.close()
        if settings["setup"]:
            print("Executing First Time Setup")
            # Do initial setup here
            settings["setup"] = False
            json.dump(settings, self.write_settings())
        else:
            return settings