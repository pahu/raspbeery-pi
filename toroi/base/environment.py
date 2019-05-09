"""Environment class

"""
import datetime

class Environment:

    def __init__(self):
        pass

    # get formatted system time 
    def time_formatted(self):
        return self.time().strftime("%Y-%m-%d %H:%M")

    # get system time
    def time(self):
        return datetime.datetime.now()