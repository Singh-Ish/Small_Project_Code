from lapp import app
from flask import render_template

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")
