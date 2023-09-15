from flask import Flask
from backend.db import db

app = Flask(__name__)
from backend.routes import service_provider
