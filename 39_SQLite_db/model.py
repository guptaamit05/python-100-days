from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db_connect import db

class Books(db.Model):
    __tablename__ = "tbl_books"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    rating: Mapped[float] = mapped_column(default=0)
