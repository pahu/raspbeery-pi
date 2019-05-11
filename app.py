"""Main app 

"""

from flask import Flask, render_template
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

if __name__ == '__main__':
    app.run(debug=True, port=6101)