from flask import Flask, render_template
import datetime, requests
app = Flask(__name__)



@app.route('/')
@app.route("/<int:id>")
def home(id=None):
    data = requests.get("https://api.npoint.io/0b5ea27fea8b7c550a9c")
    resp = data.json()
    # print(resp)
    if id:
        return render_template('post.html', posts=resp, id=id, post_time=datetime.datetime.now())
    return render_template('index.html', posts=resp, about_me="A Collection of Amit's random musings.", post_time=datetime.datetime.now())

@app.route("/about-us")
def about_us():
    return render_template("about.html", title="About Me", about_me="This is about me")


@app.route("/contact-us")
def contact_us():
    return render_template("contact.html", title="Contact Me", about_me="Have questions? I have answers")



if __name__ == "__main__":
    app.run(debug=True)