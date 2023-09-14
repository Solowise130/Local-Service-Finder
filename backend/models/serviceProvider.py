#!/usr/bin/python3
"""
this is a modules that defines a service
provider
"""
from sqlalchemy import *
from sqlalchemy.orm import relationship
from .user import Base


class ServiceProvider(Base):
    """
    this is a the model for
    service
    """
    __tablename__ = 'service_providers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone_number = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    service = Column(Integer, ForeignKey('services.id'), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP,
                        server_default=func.current_timestamp(),
                        nullable=False
                        )

    # def __init__(self, user_id, company_name, description=None, location=None):
    #     self.user_id = user_id
    #     self.company_name = company_name
    #     self.description = description
    #     self.location = location
