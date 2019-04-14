# TODO: Move to tests folder and try relative import
from sensors import DS18B20

if __name__ == '__main__':
    print ("toroi-pi: tests")
    print()
    # temperature sensors
    print ("temperature sensors")
    id = '28-041752558aff'
    temperature = DS18B20.get_temperature(id)
    print ("id: " + id)
    print ("temperature: " + str(temperature))