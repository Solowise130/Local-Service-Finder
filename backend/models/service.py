# #!/usr/bin/python3
# '''A module for service'''

# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from .user import Base


# class Service(Base):
#     '''A service class
#     '''
#     __tablename__ = 'services'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)
#     # one to many relationship
#     provider_id = Column(Integer, ForeignKey('service_providers.id'))
