from sensors import DS18B20
from flask import Flask
app = Flask(__name__)

@app.route("/")
def webapp():
    s = "<p>temperature sensors</p>"
    id = '28-041752558aff'
    temperature = DS18B20.get_temperature(id)
    s = s + "id: " + id + "<br>"
    s = s + "temperature: " + str(temperature)
    return s


