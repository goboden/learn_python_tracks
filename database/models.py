from database.db import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, nullable=False)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f'User {self.id} ({self.name}) from chat: {self.chat_id}'
