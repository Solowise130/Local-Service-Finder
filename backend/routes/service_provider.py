from backend import app
from flask import render_template, request, jsonify
from backend.models.serviceProvider import ServiceProvider
from backend import db

"""
this is the route for the
service providers
"""

@app.route('/serviceProvider/signup', methods=['POST'])
def signup():
    """
    this is a method to signup
    a service provider the 
    end point
    """
    #   {
    #   "firstName": "John",
    #   "lastName": "Doe",
    #   "mobileNumber": "1234567890",
    #   "email": "johndoe@example.com",
    #   "password": "password",
    #   "confirmPassword": "password",
    #   "termsAndConditions": true
    #   }
    json_data = request.get_json()
    if json_data['firstName'] is None:
        return jsonify({'status': 'error'})
    
    if json_data['lastName'] is None:
        return jsonify({'status': 'error'})
    
    if json_data['mobileNumber'] is None:
        return jsonify({'status': 'error'})
    
    if json_data['email'] is None:
        return jsonify({'status': 'error'})
    
    if json_data['password'] is None:
        return jsonify({'status': 'error'})
    
    if json_data['confirmPassword'] is None:
        return jsonify({'status': 'error'})
    
    if json_data['termsAndConditions'] is None:
        return jsonify({'status': 'error'})
    if json_data['password'] != json_data['confirmPassword']:
        return jsonify({'status': 'passwords do not match'})
    
    new_service_provider = ServiceProvider()
    new_service_provider.first_name = json_data['firstName']
    new_service_provider.last_name = json_data['lastName']
    #new_service_provider.location = json_data['location'] 
    new_service_provider.email = json_data['email']
    new_service_provider.phone_number = json_data['mobileNumber']
    new_service_provider.hashed_password = json_data['password']      
    #saving the service provider to the database
    dbObj = db.DB()
    dbObj.add_service_provider(new_service_provider)
    return jsonify({'status': 'success'})
    
    
