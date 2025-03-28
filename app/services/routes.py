# app/services/routes.py
from flask import render_template
from . import services

@services.route('/services/buying')
def buying():
    return render_template('services/buying.html')

@services.route('/services/selling')
def selling():
    return render_template('services/selling.html')

@services.route('/services/consultation')
def consultation():
    return render_template('services/consultation.html')
