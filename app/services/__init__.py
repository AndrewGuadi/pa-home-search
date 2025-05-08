# app/services/__init__.py
from flask import Blueprint

services = Blueprint('services', __name__, template_folder='templates')

from . import routes
