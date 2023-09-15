from backend import app
from flask import render_template, request, jsonify
from backend.models.serviceProvider import ServiceProvider
from backend import db

"""
this is the route for the
service providers
"""
print('this is from the route')

@app.route('/serviceProvider/signup', methods=['POST'])
def signup():
    """
    this is a method to signup
    a service provider the
    end point
    """
    print('hello')
    json_data = request.get_json()
    print(json_data)
    new_servce_provider = db.add_service_provider(**json_data)
    if new_servce_provider is None:
        return jsonify({'status': 'error'})
    return jsonify({'data': json_data}), 201

