# app/about/routes.py
from flask import render_template
from . import about

@about.route('/about/our_story')
def our_story():
    return render_template('about/our_story.html')

@about.route('/about/meet_the_team')
def meet_the_team():
    return render_template('about/meet_the_team.html')
