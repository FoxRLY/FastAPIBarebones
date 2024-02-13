from sqlalchemy import Engine
from sqlmodel import Session, select
from models import User

def get_all_users(engine: Engine) -> list[User]:
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users

def create_new_user(engine: Engine, user: User) -> User:
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

