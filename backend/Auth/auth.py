#!/usr/bin/python3
'''This is a module'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''returns a satled hash of the input password
    '''
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def verify_password(provided_password, stored_password_hash):
    return bcrypt.checkpw(provided_password.encode('utf-8'),
                          stored_password_hash.encode('utf-8'))
