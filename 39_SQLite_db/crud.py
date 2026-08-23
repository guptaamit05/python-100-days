from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from model import Books

def get_all_books(session: Session):
    return session.scalars(select(Books).order_by(desc(Books.rating))).all()

def get_book_by_id(session: Session, book_id: int):
    return session.get(Books, book_id)

def create_book(session: Session, title: str, rating: float, author: str):
    new_book = Books(title=title, rating=rating, author=author)
    session.add(new_book)
    session.commit()
    return new_book

def update_book(session: Session, book_id: int, title: str, rating: float, author: str):
    book = get_book_by_id(session, book_id)
    if book:
        book.title = title
        book.rating = rating
        book.author = author
        session.commit()
    return book

def delete_book(session: Session, book_id: int):
    book = get_book_by_id(session, book_id)
    if book:
        session.delete(book)
        session.commit()
        return True
    return False
