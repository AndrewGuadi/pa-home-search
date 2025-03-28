# app/reviews/routes.py
from flask import render_template
from . import reviews

@reviews.route('/reviews/video')
def video_testimonials():
    return render_template('reviews/video_testimonials.html')

@reviews.route('/reviews/written')
def written_reviews():
    return render_template('reviews/written_reviews.html')
