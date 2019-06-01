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
        self.sensor_id = cfg['fermenters'][id]['sensor_id']
        self.name = cfg['fermenters'][id]['name']
        self.target_temperature = cfg['fermenters'][id]['target_temperature']
        self.active = cfg['fermenters'][id]['active']   
        # get sensor temperature and time
        sensor = Sensor(self.sensor_id)
        self.temperature = sensor.temperature_formatted()
        self.temperature_read_time = Environment().time_formatted()