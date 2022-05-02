from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def main_route():
    return render_template("survey.html")

@app.route("/survey", methods =['POST'])
def survey():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["game"] = request.form["game"]
    session["comments"] = request.form["comments"]
    return redirect("/confirmed")

@app.route("/confirmed")
def confirmed():
    return render_template("confirmed.html")

@app.route("/back")
def back():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)