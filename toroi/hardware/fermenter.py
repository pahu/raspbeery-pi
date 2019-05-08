"""
Fermenter class
"""

import datetime
import toroi.hardware as hardware
import toroi.base as base

class Fermenter:
    
    def __init__(self,id):    
        # initialize from config.yaml
        config = base.config.Config().get_config()
        self.id = id
        self.sensor_id = config['fermenters'][0]['sensor_id']
        self.name = config['fermenters'][0]['name']
        self.target_temperature = config['fermenters'][0]['target_temperature']
        self.active = config['fermenters'][0]['active']
        # set temperature and time
        temp = hardware.sensor.get_temperature(self.sensor_id)
        temp = "{:.{}f}".format( temp, 1 )
        temp = "%s%s" % (temp, "°C")
        self.temperature = temp
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")
        self.temperature_read_time = time
