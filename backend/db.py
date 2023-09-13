#!/usr/bin/python3
'''DB module
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.user import Base
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
        DBSession = sessionmaker(bind=self._engine)
        self.__session = DBSession()

    def add_service_provider(self, **kwargs):
        '''Add service providers
        '''
        first_name = kwargs.get('firstName')
        last_name = kwargs.get('lastname')
        location = kwargs.get('location')
        email = kwargs.get('email')
        password = kwargs.get('password')
        service_id = kwargs.get('service')
        contact_num = kwargs.get('contact_num')
        description = kwargs.get('description')
        created_at = kwargs.get('created_at')

        if not all([first_name, last_name, location, email,
                password, service_id, contact_num, description,
                created_at]):
            return None
        
        new_service_provider = ServiceProvider()
        self.__session.add(new_service_provider)
        self.__session.commit()

        return new_service_provider
            
        

# test = DB()