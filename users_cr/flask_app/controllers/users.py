from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import user

#having issue with importing User vs user...one is always undefined


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

@app.route("/user/view/<int:id>")
def show_user(id):
    data = {
        "id": id
    }
    return render_template("view_user.html", user = user.get_one(data))

@app.route("/user/edit/<int:id>")
def edit_user(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user = user.get_one(data))

@app.route("/user/update",methods=["POST"])
def update():
    user.update(request.form)
    return redirect("/users")

@app.route("/user/destroy/<int:id>")
def destroy(id):
    data ={
        "id": id
    }
    user.destroy(data)
    return redirect("/users")



