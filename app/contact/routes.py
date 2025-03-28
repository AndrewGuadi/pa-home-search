# app/contact/routes.py
from flask import render_template
from . import contact

@contact.route('/contact')
def contact_form():
    return render_template('contact/contact_form.html')

@contact.route('/contact/scheduling')
def scheduling():
    return render_template('contact/scheduling.html')
