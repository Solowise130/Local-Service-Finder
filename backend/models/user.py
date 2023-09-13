#!/usr/bin/python3
'''A module for user'''

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


# class User(Base):
#     '''A user class
#     '''
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(250), nullable=False)
#     last_name = Column(String(250), nullable=False)
#     location = Column(String(250), nullable=False)
#     email = Column(String(250), nullable=False)
#     hashed_password = Column(String(250), nullable=False)
#     created_on = Column(DateTime(), default=datetime.now())
