from sensors import DS18B20
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():    
    sensorId = '28-041752558aff'
    temperature = DS18B20.get_temperature(sensorId)
    return render_template('home.html', sensorId=sensorId, temperature=temperature)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=6100)