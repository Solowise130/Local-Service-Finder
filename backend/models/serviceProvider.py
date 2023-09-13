
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

    provider_id = Column(Integer, primary_key=True, autoincrement=True)
    #user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    company_name = Column(String(255), nullable=False)
    description = Column(Text)
    location = Column(String(255))
    created_at = Column(TIMESTAMP,
                        server_default=func.current_timestamp(),
                        nullable=False
                        )
    updated_at = Column(TIMESTAMP,
                        server_default=func.current_timestamp(),
                        onupdate=func.current_timestamp(), nullable=False)

    user = relationship('User', backref='service_providers', lazy=True)
