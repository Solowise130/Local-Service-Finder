from backend import app
from flask import render_template, request, jsonify, url_for, redirect, flash, abort
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
    
    service_type = service_type.title()
    service_provider = db.get_service_providers(service_type[:-1])
    return render_template('service.html', service_provided=service_type, service_providers=service_provider)


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
        return redirect(url_for('signup'))
    
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
        flash('Please Try again with correct credentials')
        return render_template('Sign-In.html')
         
    if auth['status'] == 'success':
        login_user(auth['service_provider'])
        # print(current_user.email)
        # print(current_user)
        #return jsonify({'status': 'Your logged in'}), 200
        #reviews = db.get_reviews(auth['service_provider'].id)
        return redirect(url_for('account', id=current_user.id))
        # return render_template('Account.html', user=current_user, reviews=reviews)
    

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
    
    return redirect(url_for('index'))

@app.route('/serviceProvider/Account', methods=['GET', 'POST'])
@login_required
def account():
    '''handle account
    '''

    id = request.args.get('id')
    if (current_user.id != int(id)):
        return redirect(url_for('signin'))
    
    user = db.get_service_provider(id)
    reviews = user.reviews
    if request.method == 'POST':
        print(request.form)
        updated = db.update_service_provider(id, **request.form)
        flash('Data successfully updated', 'success')
        return redirect(url_for('account', id=current_user.id))
    
    return render_template('Account.html', user=user, reviews=reviews)


@app.route('/search', methods=['POST'])
def search():
    '''handle search for service providers
    '''
    service = request.form['service']
    
    if not service:
        return redirect(url_for('index'))
    
    service = service.title() if service[-1] == 's' else f'{service}s'.title()
    
    service_providers = db.get_service_providers(service=service[:-1])
    
    if service_providers:
        return render_template('service.html', service_provided=service, service_providers=service_providers)
    else:
        abort(404)

@app.errorhandler(404)
def handle404(error):
    '''handle 404 error'''
    return render_template('404.html'), 404
