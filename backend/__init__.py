from flask import Flask
from backend.db import DB


app = Flask(__name__)
db = DB()

from backend.routes import service_provider