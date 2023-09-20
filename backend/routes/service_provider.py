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
    return render_template('Home.html')


@app.route('/about_us')
def about():
    '''handles about us page
    '''
    return render_template('About-Us.html')


@app.route('/faqs')
def faq():
    '''handles faq page
    '''
    return render_template('FAQs.html')


@app.route('/services')
@app.route('/services/<service_type>')
def service(service_type=None):
    '''handles services page
    '''
    if not service_type:
        return render_template('Services.html')
    
    service_provider = db.get_service_providers(service_type[:-1])
    return render_template('service.html', service_provided=service_type, service_provider=service_provider)


@app.route('/contact-us')
def contact():
    '''handles services page
    '''
    return render_template('Contact-us.html')


@app.route('/serviceProvider/signup')
def signup():
    '''handles signup page
    '''
    return render_template('Sign-up-sp.html')


@app.route('/serviceProvider/signup', methods=['POST'])
def signup_post():
    """
    this is a method to signup
    a service provider the
    end point
    """

    form_data = request.form
    print(form_data)
    new_servce_provider = db.add_service_provider(**form_data)
    if new_servce_provider is None:
        flash('Email address alerady exists')
        return jsonify({'error': 'error'})
    
    print({
        'status': f'New service provider \
            {new_servce_provider.first_name} {new_servce_provider.last_name} created'
        })
    return redirect(url_for('signin'))


@app.route('/serviceProvider/signIn')
def signin():
    '''signin a service provider
    '''
    return render_template('Sign-In.html')


@app.route('/serviceProvider/signIn', methods=['POST'])
def signin_post():
    '''signin a service provider
    '''
    form_data = request.form
    auth = db.signin_service_provider(**form_data)
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
