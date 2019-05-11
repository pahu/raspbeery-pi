"""Sensor class

"""

class Sensor:

  def __init__(self, id): 
    self.id = id

  # formatted temperature
  def temperature_formatted(self):
    t = self.temperature()
    t = "{:.{}f}".format( t, 1 )
    t = "%s%s" % (t, "°C")
    return t

  # unformatted temperature
  def temperature(self):
    try:
      t = ''
      filename = 'w1_slave'
      f = open('/sys/bus/w1/devices/' + self.id + '/' + filename, 'r')
      line = f.readline() # read 1st line
      crc = line.rsplit(' ',1)
      crc = crc[1].replace('\n', '')
      if crc=='YES':
        line = f.readline() # read 2nd line
        t = line.rsplit('t=',1)
      else:
        t = 99.9
      f.close()
  
      return int(t[1])/float(1000)
  
    except:
      return 99.9