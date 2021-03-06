from lapp import app
from flask import render_template, redirect , url_for
from flask_mail import Mail,Message
from lapp import mail
from flask import flash

@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route('/sendmail',methods=['GET','POST'])
def sendmail():
    subject = 'Mail from flask server'
    msg = "testing the body message form flask mail "
    recipients = ['ishdeep.711@gmail.com']
    sender = 'ishdeepsingh@sce.carleton.ca'
    msg = Message(subject=subject, body=msg,
                  sender=sender, recipients=recipients)
    mail.send(msg)
    flash("E-mail has been sent ", "success")
    ''' adding attachment
    with app.open_resource("image.png") as fp:
        msg.attach("image.png", "image/png", fp.read())
    '''
    print("mail has been send")
    return redirect(url_for('home'))
