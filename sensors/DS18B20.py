def get_temperature(id):
  try:
    t = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      t = line.rsplit('t=',1)
    else:
      t = 99999
    f.close()
 
    return int(t[1])/float(1000)
 
  except:
    return 99999