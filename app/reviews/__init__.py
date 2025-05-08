# app/reviews/__init__.py
from flask import Blueprint

reviews = Blueprint('reviews', __name__, template_folder='templates')

from . import routes
