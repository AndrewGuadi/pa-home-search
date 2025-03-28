# app/resources/routes.py
from flask import render_template
from . import resources

@resources.route('/resources/market_trends')
def market_trends():
    return render_template('resources/market_trends.html')

@resources.route('/resources/neighborhood_guides')
def neighborhood_guides():
    return render_template('resources/neighborhood_guides.html')

@resources.route('/resources/buying_selling_tips')
def buying_selling_tips():
    return render_template('resources/buying_selling_tips.html')

@resources.route('/resources/faq')
def faq():
    return render_template('resources/faq.html')
