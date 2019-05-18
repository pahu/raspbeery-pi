# TODO: Move to tests folder and try relative import
from toroi.hardware import sensor

if __name__ == '__main__':
    print ("toroi-pi: tests")
    print()
    # temperature sensors
    print ("temperature sensors")
    id = '28-041752558aff'
    temperature = sensor.Sensor(id).temperature()
    print ("id: " + id)
    print ("temperature: " + str(temperature))