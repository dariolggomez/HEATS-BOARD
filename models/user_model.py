from typing import Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Sequence
from datetime import datetime

Base = declarative_base()
class User(Base):
    __tablename__='users'
    id = Column(Integer(), Sequence('user_id_sequence') ,primary_key=True)
    username = Column(String(25),nullable=False,unique=True)
    email = Column(String(80), unique = True, nullable = False)
    date_created = Column(DateTime(),default = datetime.now)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return f"<User username = {self.username}, email = {self.email}>"