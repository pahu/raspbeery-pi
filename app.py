"""Main app 

"""

from flask import Flask, render_template, jsonify
from toroi.hardware.device import Device
from toroi.core.config import Config

app = Flask(__name__)

# ToDo scheduler to handle 
# switch mode (heating/cooling/neutral) according to 
# settings and sensor temperatures
# PID control https://onion.io/2bt-pid-control-python/

@app.route('/')
def home():   
    title = Config().brewery_name()
    f = Device(0)
    return render_template('home.html', 
        title=title, device=f)

@app.route('/about/')
def about():
    title = Config().brewery_name()
    return render_template('about.html', 
        title = title)

@app.route('/api/device/refresh/<int:id>')
def api_device_refresh(id):
    d = Device(id)
    return jsonify({
        'temperature': d.temperature, 
        'temperature_read_time': d.temperature_read_time, 
        'mode': d.mode
    })

# @app.route('/api/device/update/<int:id><string:data>')
# def api_device_update(id, data)
#     d = Device(id)
#     # ToDo log fermenter readings on each refresh call from client
#     # ToDo switch mode (heating/cooling/neutral) according to temperature
#     return jsonify({'temperature': d.temperature, 'temperature_read_time': d.temperature_read_time })
        

if __name__ == '__main__':
    app.run(debug=True, port=6100)