from flask import (
    Flask,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
    flash,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import (
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)
import os
from db_connect import db
from dotenv import load_dotenv
from crud import get_user_by_email, create_user
from model import User


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


load_dotenv()


# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


def connect_db(database_uri="sqlite:///users.db"):
    """Application factory for easy testing configuration injection."""
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        hash_password = generate_password_hash(password, salt_length=8, method="scrypt")
        user = get_user_by_email(db.session, email)
        if user:
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for("login"))

        new_user = create_user(db.session, name, email, hash_password)
        if new_user:
            login_user(new_user)
            return redirect(url_for("secret_file"))

    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = get_user_by_email(db.session, email)
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for("login"))
        elif not check_password_hash(user.password, password):
            flash("Password incorrect, please try again.")
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("secret_file"))
        # return render_template("login.html", not_registered=True)

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route("/logout")
def logout():
    logout_user()
    return render_template("login.html")


@app.route("/secret")
@login_required
def secret_file():
    return render_template(
        "secrets.html", name=current_user.name, logged_in=current_user.is_authenticated
    )


@app.route("/download")
@login_required
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    connect_db()
    app.run(debug=True)
