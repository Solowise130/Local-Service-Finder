#!/usr/bin/python3
'''A module for review'''

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from models.user import Base


class Review(Base):
    '''A review class
    '''
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    # userId = Column(Integer, 
    #                 ForeignKey('users.id'), nullable=False)
    serviceProviderId = Column(Integer,
                               ForeignKey('service_providers.id'), nullable=False)
    rating = Column(Integer, default=0)
    comment = Column(String(250), nullable=False)