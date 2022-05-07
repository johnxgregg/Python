from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import user

#import models here

#we will define our routes in here

@app.route("/users")
def all_users_page():
    return render_template("all_users.html", all_users = user.User.get_all_users())

@app.route("/users/new")
def add_user_page():
    return render_template("add_user.html")

@app.route("/users/add_to_db", methods=["POST"])
def add_user_to_db():
    
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    user.User.add_user(data)
    return redirect("/users")