from lapp import app
from flask import render_template, render_template_string, request,jsonify
from lapp.models import user
from lapp.forms import userForm
from bson import ObjectId

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():

    if not user.objects.all():
        name = "Ish"
        email= "Ishdeepsingh@sce.carleton.ca"

        u = user(name = name , email= email )
        u.save()

    users = user.objects.all()
    return render_template("index.html" , users=users)

'''
@app.route("/usercreate" , methods=['GET','POST'])
def usercreate():
    form = userForm()
    context = {'form': form}

    html_form = render_template_string("createuser.html",context,request=request)
    return jsonify({'html_form': html_form})
'''

@app.route('/user',methods=['GET','POST'])
def getpost():
    if request.method=='GET':
        o=[]
        for i in user.objects.all():
            o.append({"id":str(ObjectId(i["id"])),  "name":i["name"],"email":i["email"],"role":i["role"]})

        return jsonify(o)
    elif request.method=="POST":
        email = request.json["email"]
    
        if  user.objects(email=email):
            return jsonify("email already exist")

        u = user(name=request.json["name"],email=request.json["email"],role=request.json["role"])
        #u.save()
        return jsonify (" the user "+ request.json["email"]+" has been added to database")

@app.route('/user/<id>',methods=['GET','DELETE','PUT'])
def delteput(id):
    if request.method=="DELETE":
        u = user.objects(email=str(id))
        if not u:
            return jsonify(" Id does not exist in the database")

        u.delete()
        return jsonify(" deleted the id "+ id + "  from  database")
    
    elif request.method=="PUT":
        u = user.objects(email=request.json["email"]).first()
        u.name = request.json["name"]
        u.role = request.json["role"]
        u.email = request.json["email"] # this will never run 

        u.save()
        return jsonify(u)

    elif request.method=="GET":
        u= user.objects(email = str(id))
        return jsonify(u)
        
