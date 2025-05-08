# app/resources/__init__.py
from flask import Blueprint

resources = Blueprint('resources', __name__, template_folder='templates')

from . import routes
