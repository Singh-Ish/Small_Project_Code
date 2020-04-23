from lapp import app, mail 
from flask import render_template, request, json, Response, redirect, url_for, session, jsonify
from flask_mail import Mail,Message
from flask import flash
from lapp.models import User,Role
from lapp.forms import LoginForm, RegisterForm
from flask_user import current_user, roles_required, login_required,UserManager,UserMixin
#from lapp.forms import LoginForm, RegisterForm

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
def adash():
    userId = session.get('userId')

    user = User.objects(userId=userId).first()
    #print(user.roles)
    if (user.roles == 'admin'):
        return render_template("sdash.html")

    flash("you dont have access to this page redirected to login page ", "danger")

    return render_template("adash.html") 

@app.route('/sdash/')
def sdash():

    userId = session.get('userId')

    user = User.objects(userId=userId).first()
    #print(user.roles)  
    #if (user.roles == 'student'):
        #return render_template("sdash.html")

    flash("you dont have access to this page redirected to login page ", "danger")

    return redirect(url_for('home'))

##################### login routes 

@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('home'))
        
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and password == user.get_password(password):
            flash(f"{user.firstName}, you are successfully logged in!", "success")
            session['userId'] = user.userId
            session['username'] = user.firstName
            # implement various routes depemnding on the security roles
            return redirect("/sdash")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("auth/login.html", title="Login", form=form, login=True)


# once register it should go to the admin to approve and connect the supervisor to the project
@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get('username'):
        return redirect(url_for('home'))
    # check if the student is registered or not using a unique user Id
    form = RegisterForm()
    if form.validate_on_submit():
        userId = form.userId.data
        email = form.email.data
        password = form.password.data
        firstName = form.firstName.data
        lastName = form.lastName.data
        print(userId)
        print(email)
        user = User(userId=userId, email=email,
                    firstName=firstName, lastName=lastName)
        user.set_password(password)
        user.save()

        role = Role(userId=userId)
        role.save()
        flash("you are successfully registeres!", "success")
        return redirect(url_for('sdash'))
    return render_template("auth/register.html", title="Register", form=form, register=True)


@app.route("/logout")
def logout():
    session['userId'] = False
    session.pop('username', None)
    flash("you are successfully logged out !", "success")
    return redirect(url_for('home'))
