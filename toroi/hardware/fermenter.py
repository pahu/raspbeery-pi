"""Fermenter class

"""

from .sensor import Sensor
from toroi.core.environment import Environment
from toroi.core.config import Config

class Fermenter:  
    def __init__(self,id):    
        # initialize from config.yaml
        cfg = Config().get_config()
        self.id = id
        self.sensor_id = cfg['fermenters'][0]['sensor_id']
        self.name = cfg['fermenters'][0]['name']
        self.target_temperature = cfg['fermenters'][0]['target_temperature']
        self.active = cfg['fermenters'][0]['active']   
        # get sensor temperature and time
        sensor = Sensor(self.sensor_id)
        self.temperature = sensor.temperature_formatted()
        self.temperature_read_time = Environment().time_formatted()