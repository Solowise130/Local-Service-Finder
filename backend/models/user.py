from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime



Base = declarative_base()

class User(Base):
    '''A user class
    '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    hashed_password = Column(String(250), nullable=True)
    created_on = Column(DateTime(), default=datetime.now())