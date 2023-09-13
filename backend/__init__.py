from flask import Flask
app = Flask(__name__, template_folder='./../frontend/templates')
from .routes import service_provider