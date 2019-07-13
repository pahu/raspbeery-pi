"""Device class
Kettle, Fridge etc.

"""

from .sensor import Sensor
from toroi.core.environment import Environment
from toroi.core.config import Config

class Device:  
    def __init__(self,id):    
        # initialize from config.yaml
        cfg = Config().get_config()
        self.id = id
        self.sensor_id = cfg['device'][id]['sensor_id']
        self.name = cfg['device'][id]['name']
        self.target_temperature = cfg['device'][id]['target_temperature']
        self.active = cfg['device'][id]['active']   
        # get sensor temperature and time
        sensor = Sensor(self.sensor_id)
        self.temperature = sensor.temperature_formatted()
        self.temperature_read_time = Environment().time_formatted()
        self.set_mode(sensor)

    def set_mode(self, sensor):
        self.mode = "neutral"
        #if (sensor.temperature + .5) > self.target_temperature:
        #    self.mode = "cooling"
        #if (sensor.temperature - .5) < self.target_temperature:
        #    self.mode = "heating"