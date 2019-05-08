import datetime
import toroi.hardware as hardware
import toroi.base as base

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():   
    config = base.config.Config().get_config()
    title = config['brewery']['name']
    
    f = hardware.fermenter.Fermenter(0)

    return render_template('home.html', 
        title=title, fermenter=f)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=6100)