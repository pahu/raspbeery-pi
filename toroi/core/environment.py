"""Environment class

"""

import datetime
from .config import Config

class Environment:

    def __init__(self):
        pass

    # formatted system time 
    def time_formatted(self):
        return self.time().strftime("%Y-%m-%d %H:%M")

    # unformatted system time
    def time(self):
        return datetime.datetime.now()