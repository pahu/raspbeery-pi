"""Main app 

"""

from flask import Flask, render_template, jsonify
from toroi.hardware.fermenter import Fermenter
from toroi.core.config import Config

app = Flask(__name__)

@app.route("/")
def home():   
    title = Config().brewery_name()
    f = Fermenter(0)
    return render_template('home.html', 
        title=title, fermenter=f)

@app.route('/about/')
def about():
    title = Config().brewery_name()
    return render_template('about.html', 
        title = title)

@app.route('/api/fermenter/refresh/<int:id>')
def api_fermenter_refresh(id):
        f = Fermenter(id)
        # ToDo log fermenter readings on each refresh call from client
        # ToDo switch mode (heating/cooling/neutral) according to temperature
        return jsonify({'temperature': f.temperature, 'temperature_read_time': f.temperature_read_time })

if __name__ == '__main__':
    app.run(debug=True, port=6101)