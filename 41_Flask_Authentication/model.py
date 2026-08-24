from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from db_connect import db
from flask_login import UserMixin


# CREATE TABLE IN DB.
class User(UserMixin, db.Model):
    __tablename__ = "tbl_user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True)
    password: Mapped[str] = mapped_column(String(500))
    name: Mapped[str] = mapped_column(String(250))
