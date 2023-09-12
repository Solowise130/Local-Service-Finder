#!/usr/bin/python3
'''DB module
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import Base, User
from models.service import Service
from models.review import Review
from models.serviceProvider import ServiceProvider

class DB:
    '''DB class
    '''

    def __init__(self) -> None:
        '''Initialize a new DB instance
        '''
        db = 'service_finder_db'
        user = 'user'
        password = 'password'
        host = 'localhost'
        self._engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db}',
            pool_pre_ping=True
        )
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)


# test = DB()