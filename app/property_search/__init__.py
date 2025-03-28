# app/property_search/__init__.py
from flask import Blueprint

property_search = Blueprint('property_search', __name__)

from . import routes
