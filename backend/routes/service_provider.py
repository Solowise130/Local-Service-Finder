from backend import app
from flask import render_template, request, jsonify
from backend.models.serviceProvider import ServiceProvider
from backend.db import db
from flask_login import (LoginManager, UserMixin, login_user,
                         login_required, logout_user, current_user)


"""
this is the route for the
service providers
"""

app.secret_key = '12345'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/serviceProvider/signup', methods=['POST'])
def signup():
    """
    this is a method to signup
    a service provider the
    end point
    """

    json_data = request.get_json()
    new_servce_provider = db.add_service_provider(**json_data)
    if new_servce_provider is None:
        return jsonify({'status': 'error'})
    return jsonify(
        {'status': f'New service provider {
            new_servce_provider.first_name
            } {
                new_servce_provider.last_name
                } created'}
        ), 201


@app.route('/serviceProvider/signIn', methods=['POST'])
def sigin():
    '''signin a service provider
    '''
    json_data = request.get_json()
    auth = db.signin_service_provider(**json_data)
    if auth['status'] == 'success':
        login_user(auth['service_provider'])
        return jsonify({'status': 'Your logged in'}), 200
    return jsonify(auth), 401


def signOut():
    '''signout a service provider
    '''
    logout_user()
    return jsonify({'status': 'success'}), 200
