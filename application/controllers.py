from flask import Flask,request
from flask import render_template,redirect
from flask import current_app as app
from .database import *
from .models import *

@app.route("/")
@app.route("/home")
def home():
    users = User.query.all()
    return render_template("home.html",users=users)
 
@app.route("/contact")
def contact():
    return render_template("contact.html")
 
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html",error_age="",error_roll="",error_mob="")
    else:
        name=request.form.get("name")
        dob=request.form.get("dob")
        roll_no=request.form.get("roll")
        mobile=request.form.get("mobile")
        email=request.form.get("mail")
        sex=request.form["gender"]
        branch=request.form.get("branch")
        e1=""
        e2=""
        e3=""
        if dob>"2004-01-05" or dob<"2002-01-04":
            e1="Doesn't match the age criteria"
        if len(roll_no)!=9 or roll_no[0] not in ['B','M','P'] or not(roll_no[1:6].isnumeric()) or not (roll_no[7:8].isalpha()):
            e2="invalid roll number"
        if len(mobile)!=10:
            e3="enter a valid mobile number(without country code)"
        if e1=="" and e2=="" and e3=="":
            p=User(name=name,dob=dob,roll=roll_no,branch=branch,mobile=mobile,email=email,sex=sex)
            db.session.add(p)
            db.session.commit()
            return redirect("/")
        else:
            return render_template("register.html",error_age=e1,error_roll=e2,error_mob=e3)