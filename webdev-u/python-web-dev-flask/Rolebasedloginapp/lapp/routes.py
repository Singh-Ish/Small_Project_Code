from lapp import app, mail 
from flask import render_template, request, json, Response, redirect, url_for, session, jsonify
from flask_mail import Mail,Message
from flask import flash
from lapp.models import User
from flask_user import current_user,roles_required, login_required,UserManager,UserMixin


@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route('/sendmail',methods=['GET','POST'])
def sendmail():
    #subject = 'Mail from flask server'
   # msg = "testing the body message form flask mail "
    #msg = Message(subject=subject,body=msg, sender='ishdeepsingh@sce.carleton.ca', recipients=['ishdeep.711@gmail.com'])
  #  mail.send(msg)
    ''' adding attachment
    with app.open_resource("image.png") as fp:
        msg.attach("image.png", "image/png", fp.read())
    '''
    if request.method == 'POST':
        print("mail has been send")
        flash("Email has been sent .", "success")
    
    return redirect(url_for('home'))


@app.route('/adash')
@login_required
def adash():
    return render_template("adash.html") 

@app.route('/sdash/')
@login_required
def sdash():
    return render_template("sdash.html")

