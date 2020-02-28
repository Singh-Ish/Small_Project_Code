from lapp import app
from flask import render_template, redirect , url_for
from flask_mail import Mail,Message
from lapp import mail

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route('/sendmail',methods=['GET','POST'])
def sendmail():
    subject = 'Mail from flask server'
    msg = "testing the body message form flask mail "
    msg = Message(subject=subject,body=msg, sender='ishdeepsingh@sce.carleton.ca', recipients=['ishdeep.711@gmail.com'])
    mail.send(msg)
    ''' adding attachment
    with app.open_resource("image.png") as fp:
        msg.attach("image.png", "image/png", fp.read())
    '''
    print("mail has been send")
    return redirect(url_for('home'))
