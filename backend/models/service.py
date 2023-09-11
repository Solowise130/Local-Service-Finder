#!/usr/bin/python3
'''A module for service'''

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from models.user import Base


class Service(Base):
    '''A service class
    '''
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    service_providers = relationship('ServiceProvider') # one to many relatioship