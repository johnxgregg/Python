from flask_app import app
from flask_app.controllers import users  #import all my controller files

if __name__=="__main__":
    app.run(debug=True)

#just this for server.py file