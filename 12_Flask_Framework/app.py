

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index page of Flask application ok."

@app.route("/welcome")
def welcome():
    return "Welcome to Flask application ok."



if __name__=="__main__":
    app.run(debug=True)