from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def render_list():
    users = [
        {'first_name': 'John', 'last_name' : 'Gregg'},
        {'first_name': 'Yurie', 'last_name' : 'Gregg'},
        {'first_name': 'Ryan', 'last_name' : 'Markel'},
        {'first_name': 'Soo', 'last_name' : 'Markel'}
    ]
    return render_template("index.html", users = users)




if __name__=="__main__":
    app.run(debug=True)