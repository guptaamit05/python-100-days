from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
from dotenv import load_dotenv
import os

from crud import get_all_books,create_book
from db_connect import db

app = Flask(__name__)
load_dotenv()


def connect_db(database_uri="sqlite:///all_books.db"):
    """Application factory for easy testing configuration injection."""
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()


## Flask_WTF Form for Add Book
class BookAddForm(FlaskForm):
    book_name = StringField(name='book_name', validators=[DataRequired('Name is required.')])
    book_author = StringField(name='book_author', validators=[DataRequired('Author is required.')])
    book_rating = FloatField(name='book_rating', validators=[DataRequired('Rating is required.' ), NumberRange(min=1, max=10,  message='Rating must be positive (min 1 and max 10).')
])
    submit_btn = SubmitField(name='add_book')
    


app.secret_key = os.getenv("SECRET_KEY")
@app.route('/', methods=['GET'])
def home():
    all_books = get_all_books(db.session)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    
    bookForm = BookAddForm()
    if bookForm.validate_on_submit():
        # print(bookForm.book_name.data)
        create_book(
            session=db.session,
            title=bookForm.book_name.data,
            rating=float(bookForm.book_rating.data),
            author=bookForm.book_author.data
        )
        return redirect(url_for('home'))
    
    return render_template("add.html", form=bookForm)


if __name__ == "__main__":
    connect_db()
    app.run(debug=True)
