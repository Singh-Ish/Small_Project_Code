from lapp import app
from flask import render_template,jsonify
from lapp.models import user

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/user",methods=('GET','POST'))
def luser():
    u = user.objects.all()

    return jsonify(u)