from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from model import User


def get_all_user(session: Session):
    return session.scalars(select(User).order_by(desc(User.name))).all()


def get_user_by_id(session: Session, user_id: int):
    return session.get(User, user_id)


def get_user_by_email(session: Session, email: str):
    return session.scalars(select(User).where(User.email == email)).first()


def create_user(session: Session, name: str, email: str, password: str):
    new_user = User(name=name, email=email, password=password)
    session.add(new_user)
    session.commit()
    return new_user


def update_user(session: Session, user_id: int, password: str):
    user = get_user_by_id(session, user_id)
    if user:
        user.password = password
        session.commit()
    return user


def delete_user(session: Session, user_id: int):
    user = get_user_by_id(session, user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    return False
