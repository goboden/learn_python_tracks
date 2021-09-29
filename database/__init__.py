from database.db import db_session
from database.models import User


def add_user(id, name, chat_id):
    user = User(id=id, chat_id=chat_id, name=name)
    db_session.add(user)
    db_session.commit()
