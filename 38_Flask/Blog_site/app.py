from flask import Flask, render_template
import random, datetime, requests
app = Flask(__name__)


@app.get("/")
def home():
    random_num = random.randint(0,100)
    return render_template("index.html", num=random_num, year=datetime.datetime.now().year)


@app.get("/guess/<name>")
def guess_name(name):
    url = f'https://api.agify.io?name={name}'
    data = requests.get(url)
    data = data.json()
    return render_template("guess.html", data=data)


@app.route('/blog')
@app.route("/blog/<int:id>")
def get_blog(id=None):
    data = requests.get("https://api.npoint.io/0b5ea27fea8b7c550a9c")
    resp = data.json()
    # print(resp)
    if id:
        return render_template('blog.html', posts=resp, id=id)
    return render_template('blog.html', posts=resp)


if __name__ == "__main__":
    app.run(debug=True)