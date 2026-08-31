
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get_test", methods=['GET'])
def get_test():
    return "This is GET method..."

@app.route("/form", methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form["name"]
        return f"Hello {name}"
    return render_template("form.html")

# Variable Rule..
@app.route("/source/<user>")
def source(user):
    return f"This is user name : {user}"



@app.route("/source_int/<int:user>")  ## you have to give integer value only... this is variable rule...
def source_int(user):
    return f"This is user name : {user}"


@app.route("/success/<int:score>")
def success(score):
    # return f"This is user name : {score}"
    res = ""
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"
    data = {'score':score, 'msg':res}
    return render_template('result.html', results=data)



if __name__ == "__main__":
    app.run(debug=True)