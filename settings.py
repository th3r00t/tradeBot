import os
import sys
import json

class Settings():


    def __init__(self):
        self.setup()

    def read_settings(self):
        return open('settings.json', 'r')

    def write_settings(self):
        return open('settings.json', 'w')

    def setup(self):
        settings_file = self.read_settings()
        self.settings = json.load(settings_file)
        settings_file.close()
        if self.settings["setup"]:
            print("Executing First Time Setup")
            # Do initial setup here
            settings["setup"] = False
            json.dump(settings, self.write_settings())
        else:
            settings_file.close()
            return self
