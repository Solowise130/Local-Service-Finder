from flask import Flask
from flask_login import LoginManager
from backend.db import db

app = Flask(__name__)

app.secret_key = '12345'

login_manager = LoginManager()
login_manager.init_app(app)

from backend.routes import service_provider

@login_manager.user_loader
def load_user(user_id):
    user = db.get_service_provider(int(user_id))
    return user