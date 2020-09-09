from lapp import app
from flask import render_template, request ,Flask, url_for

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/about",methods=['GET','POST'])
def about():
    return render_template("about.html")