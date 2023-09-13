from flask import Flask
from .routes import *
from backend.db import DB


app = Flask(__name__)
db = DB()
