from backend import app
from flask import render_template, request, jsonify
from backend.models.serviceProviders import ServiceProvider
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

    new_servce_provider = db.add_service_provider(**json_data)
    if new_servce_provider is None:
        return jsonify({'status': 'error'})
    
    return jsonify({'status': 'success'})
    
    
