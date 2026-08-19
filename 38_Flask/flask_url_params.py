from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return "Hii from Home Page.."


def decorator_auth(fun):
    def wrapper(*args, **kwargs):
        if False:
            print("Logged in user...")
            return fun(*args, **kwargs)
        else:
            return "Not Logged in"
    return wrapper


@app.get("/bye/<username>")
def bye(username):
    return f"Bye User: {username}"

@app.get("/about_us")
@decorator_auth
def about_us():
    return "You are logged in"


if __name__ == "__main__":
    app.run(host='localhost', debug=True)