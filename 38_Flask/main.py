from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    # app.run(host="localhost", port=2323)   # when you run app using : python main.py command..
    app.run()  #  when you run command using:   flask run


