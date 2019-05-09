"""Main app 

"""

from toroi.hardware import fermenter
from toroi.core import config
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():   
    cfg = config.Config().get_config()
    title = cfg['brewery']['name']
    f = fermenter.Fermenter(0)
    return render_template('home.html', 
        title=title, fermenter=f)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=6100)