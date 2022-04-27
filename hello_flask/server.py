from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("Hello World!")

@app.route("/dojo")
def dojo():
    return ("Dojo!")

@app.route("/say/<word>")
def say(word):
    return "hello " + word

@app.route("/repeat/<string:hello>/<int:num>")
def repeat(hello, num):
    return f"Hello {hello * num}"

@app.route("/repeat/<string:dogs>/<int:num>")
def repeat(dogs, num):
    return f"Hot {dogs * num}"

@app.route("/repeat/<string:bye>/<int:num>")
def repeat(bye, num):
    return f"bye {bye * num}"

if __name__=="__main__":
    app.run(debug=True)

