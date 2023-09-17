#!/usr/bin/python3
"""
this is a modules that defines a service provider
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
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    services = Column(String(250), nullable=False)
    reviews = relationship('Review', backref='service_providers',
                           cascade='all, delete, delete-orphan'
                           )
    created_at = Column(TIMESTAMP,
                        server_default=func.current_timestamp(),
                        nullable=False
                        )

    def get_id(self):
        # Return the unique identifier for the user,
        # which is typically the user's ID
        return str(self.id)
