"""
System configuration class
"""

import yaml

class Config:

    def __init__(self):
        pass

    # get yaml config file
    def get_config(self):
        with open("config.yml", 'r') as ymlConfig:
            return yaml.load(ymlConfig)