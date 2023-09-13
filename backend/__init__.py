from flask import Flask
from .routes import service_provider
from db import DB


app = Flask(__name__, template_folder='./../frontend/templates')
db = DB()
