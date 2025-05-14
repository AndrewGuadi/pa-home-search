# app/contact/forms.py (Contact and appointment scheduling forms)
# app/contact/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
    name = StringField(
        'Full Name',
        validators=[DataRequired(), Length(max=100)]
    )
    email = StringField(
        'Email Address',
        validators=[DataRequired(), Length(max=120)]
    )
    phone = StringField(
        'Phone Number',
        validators=[DataRequired(), Length(max=20)]
    )
    service = SelectField(
        'Service You’re Interested In',
        choices=[
            ('buying', 'Buying'),
            ('selling', 'Selling'),
            ('consultation', 'Consultation / CMA'),
        ],
        validators=[DataRequired()]
    )
    how_heard = SelectField(
        'How Did You Hear About Us?',
        choices=[
            ('google', 'Google Search'),
            ('referral', 'Friend / Referral'),
            ('social', 'Social Media'),
            ('event', 'Local Event'),
            ('other', 'Other'),
        ],
        validators=[DataRequired()]
    )
    priority = SelectField(
        'Most Important Quality in Your Agent',
        choices=[
            ('communication', 'Clear Communication'),
            ('negotiation', 'Strong Negotiation'),
            ('local', 'Local Market Knowledge'),
            ('responsiveness', 'Fast Response Time'),
            ('marketing', 'Marketing Expertise'),
            ('other', 'Other'),
        ],
        validators=[DataRequired()]
    )
    preferred_contact = RadioField(
        'Preferred Contact Method',
        choices=[
            ('email', 'Email'),
            ('phone', 'Phone'),
        ],
        validators=[DataRequired()]
    )
    best_time = SelectField(
        'Best Time to Reach You',
        choices=[
            ('morning', 'Morning'),
            ('afternoon', 'Afternoon'),
            ('evening', 'Evening'),
        ],
        validators=[DataRequired()]
    )
    message = TextAreaField(
        'Tell Us More (optional)',
        validators=[Length(max=500)]
    )
    submit = SubmitField('Send Message')