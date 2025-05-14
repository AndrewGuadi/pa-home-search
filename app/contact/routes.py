# app/contact/routes.py
from flask import render_template, request, flash, redirect, url_for
from .forms import ContactForm
from . import contact

@contact.route('/contact', methods=['GET', 'POST'])
def contact_form():
    form = ContactForm()
    if form.validate_on_submit():
        # handle submission: send email, log to DB, etc.
        flash('Thanks—your message is on its way!')
        return redirect(url_for('contact.contact_form'))
    return render_template('contact/contact_form.html', form=form)

@contact.route('/contact/scheduling')
def scheduling():
    return render_template('contact/scheduling.html')
