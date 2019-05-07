import datetime
import yaml
from toroi.sensor import DS18B20
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():   
    config = get_config()
    title = config['brewery']['name']
    sensorId = config['fermenters'][0]['sensorId']
    name = config['fermenters'][0]['name']
    targetTemp = config['fermenters'][0]['targetTemp']
    active = config['fermenters'][0]['active']
    temperature = DS18B20.get_temperature(sensorId)
    temperature = "{:.{}f}".format( temperature, 1 ) 
    temperature = "%s%s" % (temperature, "°C")
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    return render_template('home.html', 
        title=title, name=name,
        temperature=temperature, time=time, 
        targetTemp=targetTemp, active=active)

@app.route('/about/')
def about():
    return render_template('about.html')


# get yaml config file
def get_config():
    with open("config.yml", 'r') as ymlConfig:
        return yaml.load(ymlConfig)


if __name__ == '__main__':
    app.run(debug=True, port=6100)

