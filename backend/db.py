#!/usr/bin/python3
'''DB module
'''
# from flask_login import login_user
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.models.user import Base
# from backend.models.service import Service
from backend.models.review import Review
from backend.models.serviceProvider import ServiceProvider
from backend.Auth.auth import hash_password, verify_password


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
        # Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        DBSession = sessionmaker(bind=self._engine)
        self.__session = DBSession()

    def add_service_provider(self, **kwargs):
        '''Add service providers
        '''
        if not kwargs:
            return None

        first_name = kwargs.get('firstName')
        last_name = kwargs.get('lastName')
        location = kwargs.get('location')
        email = kwargs.get('email')
        password = kwargs.get('password')
        service = kwargs.get('service')
        contact_num = kwargs.get('contact_num')
        description = kwargs.get('description')
        created_at = kwargs.get('created_at')

        if not all([first_name, last_name, location,
                    email, password, service, contact_num]):
            return None
        
        # check if service provider exists
        provider = self.__session.query(ServiceProvider).filter(
            ServiceProvider.email == email
        ).first()
        if provider:
            return None
        
        new_service_provider = ServiceProvider()
        new_service_provider.first_name = first_name
        new_service_provider.last_name = last_name
        new_service_provider.email = email
        new_service_provider.location = location
        new_service_provider.phone_number = contact_num
        new_service_provider.description = description
        new_service_provider.created_at = created_at
        new_service_provider.hashed_password = hash_password(password)
        new_service_provider.services = service

        self.__session.add(new_service_provider)
        self.__session.commit()

        return new_service_provider

    def add_review(self, **kwargs):
        '''Add a review
        '''
        if not kwargs:
            return None

        serviceProviderId = kwargs.get('serviceProviderId')
        rating = kwargs.get('rating')
        comment = kwargs.get('comment')

        if not all([rating, comment]):
            return None

        new_review = Review(serviceProviderId=serviceProviderId,
                            rating=rating, comment=comment)

        self.__session.add(new_review)
        self.__session.commit()
        return new_review

    def get_service_provider(self, id):
        '''Get service provider by Id
        '''
        if not id:
            return None

        service_provider = self.__session.query(ServiceProvider).filter(
            ServiceProvider.id == id
        ).first()

        if service_provider:
            return service_provider
        return None

    def signin_service_provider(self, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')
        if not email or not password:
            return {'status': 'email or password not provided'}
        service_provider = self.__session.query(ServiceProvider).filter(
            ServiceProvider.email == email
            ).first()
        # print(service_provider.hashed_password)
        if not service_provider:
            return None
        if verify_password(password, service_provider.hashed_password):
            service_provider.is_active = True
            return {'status': 'success', 'service_provider': service_provider}
        return None


db = DB()
