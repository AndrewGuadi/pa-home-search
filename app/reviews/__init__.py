# app/reviews/__init__.py
from flask import Blueprint

reviews = Blueprint('reviews', __name__)

from . import routes
