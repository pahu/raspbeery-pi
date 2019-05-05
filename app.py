import datetime
import yaml
from toroi.sensor import DS18B20
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():   
    with open("config.yml", 'r') as ymlConfig:
        cfg = yaml.load(ymlConfig)

    title = cfg['brewery']['name']
    
    sensorId = cfg['fermenters'][0]['sensorId']
    name = cfg['fermenters'][0]['name']
    temperature = DS18B20.get_temperature(sensorId)
    temperature = "{:.{}f}".format( temperature, 1 ) 
    temperature = "%s%s" % (temperature, "°C")
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    return render_template('home.html', 
        title=title, name=name,
        temperature=temperature, time=time)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=6100)