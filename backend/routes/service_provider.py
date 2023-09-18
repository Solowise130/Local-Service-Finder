from backend import app
from flask import render_template, request, jsonify, url_for, redirect, flash
from backend.models.serviceProvider import ServiceProvider
from backend.db import db
from flask_login import (login_user,
                         login_required, logout_user, current_user)


"""
this is the route for the
service providers
"""


@app.route('/')
def index():
    '''handles the index page
    '''
    pass

@app.route('/serviceProvider/signup')
def signup():
    '''handles signup page
    '''
    pass
    # return render_template('signup.html')


@app.route('/serviceProvider/signup', methods=['POST'])
def signup_post():
    """
    this is a method to signup
    a service provider the
    end point
    """

    json_data = request.get_json()
    new_servce_provider = db.add_service_provider(**json_data)
    if new_servce_provider is None:
        flash('Email address alerady exists')
        return jsonify({'error': 'error'})
        # return redirect(url_for('signup'))
    
    print({
        'status': f'New service provider \
            {new_servce_provider.first_name} {new_servce_provider.last_name} created'
        })
    return jsonify({'success': 'success'})
    # return redirect(url_for('signin'))


@app.route('/serviceProvider/signIn')
def signin():
    '''signin a service provider
    '''
    pass
    # return render_template('login.html')


@app.route('/serviceProvider/signIn', methods=['POST'])
def signin_post():
    '''signin a service provider
    '''
    json_data = request.get_json()
    auth = db.signin_service_provider(**json_data)
    if not auth:
        return jsonify({'error': 'error'}), 401
    if auth['status'] == 'success':
        login_user(auth['service_provider'])
        print(current_user.email)
        return jsonify({'status': 'Your logged in'}), 200
    


@app.route('/logout')
@login_required
def signOut():
    '''signout a service provider
    '''
    user = current_user
    print(user.email)
    if current_user.is_authenticated:
        print(True)

    logout_user()
    
    return jsonify({'status': 'success'}), 200
