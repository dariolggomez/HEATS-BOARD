from typing import Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Sequence
from datetime import datetime

Base = declarative_base()
class User(Base):
    __tablename__='users'
    id = Column(Integer(), Sequence('user_id_sequence') ,primary_key=True)
    username = Column(String(25),nullable=False,unique=True)
    password = Column(String(80),nullable=False,unique=False)
    email = Column(String(80), unique = True, nullable = False)
    role = Column(Integer(), nullable = False, unique = False)
    date_created = Column(DateTime(),default = datetime.now)

    def __init__(self, username, password, email, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self) -> str:
        return f"<User username = {self.username}, email = {self.email}>"