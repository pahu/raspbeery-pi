"""Fermenter class docstring

"""

#import toroi.hardware. as hardware
import toroi.base as base
from .sensor import Sensor

class Fermenter:
    
    def __init__(self,id):    
        # initialize from config.yaml
        config = base.config.Config().get_config()
        self.id = id
        self.sensor_id = config['fermenters'][0]['sensor_id']
        self.name = config['fermenters'][0]['name']
        self.target_temperature = config['fermenters'][0]['target_temperature']
        self.active = config['fermenters'][0]['active']   
        # get sensor temperature and time
        sensor = Sensor(self.sensor_id)
        self.temperature = sensor.temperature_formatted()
        self.temperature_read_time = base.environment.Environment().time_formatted()