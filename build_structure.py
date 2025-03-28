import os

# Define the project structure with file paths and optional initial content
structure = {
    'run.py': """\
# run.py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
""",
    'requirements.txt': "# Add your Python dependencies here\nflask\n",
    'config.py': """\
# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    # Add your configuration variables (e.g., database URIs, API keys) here
""",
    '.env': "# Environment variables go here\nSECRET_KEY=your_secret_key\n",
    'instance/': None,  # Directory only, no file content
    'app/__init__.py': """\
# app/__init__.py
from flask import Flask
from .extensions import init_extensions

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize extensions
    init_extensions(app)
    
    # Import and register blueprints
    from .main import main as main_blueprint
    from .property_search import property_search as property_blueprint
    from .services import services as services_blueprint
    from .reviews import reviews as reviews_blueprint
    from .about import about as about_blueprint
    from .resources import resources as resources_blueprint
    from .contact import contact as contact_blueprint
    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(property_blueprint)
    app.register_blueprint(services_blueprint)
    app.register_blueprint(reviews_blueprint)
    app.register_blueprint(about_blueprint)
    app.register_blueprint(resources_blueprint)
    app.register_blueprint(contact_blueprint)
    
    return app
""",
    'app/extensions.py': """\
# app/extensions.py
# Initialize and configure Flask extensions here

def init_extensions(app):
    # Example: Initialize SQLAlchemy, Migrate, LoginManager, etc.
    pass
""",
    'app/models.py': """\
# app/models.py
# Define your data models here (e.g., User, Property, etc.)
""",
    # Blueprints directories and files
    'app/main/__init__.py': """\
# app/main/__init__.py
from flask import Blueprint

main = Blueprint('main', __name__)

from . import routes
""",
    'app/main/routes.py': """\
# app/main/routes.py
from flask import render_template
from . import main

@main.route('/')
def index():
    return render_template('main/index.html')
""",
    'app/main/forms.py': "# app/main/forms.py (Optional forms for main blueprint)\n",
    'app/main/templates/main/index.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to My Real Estate Site</h1>
</body>
</html>
""",
    'app/property_search/__init__.py': """\
# app/property_search/__init__.py
from flask import Blueprint

property_search = Blueprint('property_search', __name__)

from . import routes
""",
    'app/property_search/routes.py': """\
# app/property_search/routes.py
from flask import render_template
from . import property_search

def get_listings_for_city(city):
    # Placeholder function - integrate MLS data here
    return []

@property_search.route('/property_search/<city>')
def city_page(city):
    listings = get_listings_for_city(city)
    return render_template('property_search/city_page.html', city=city, listings=listings)
""",
    'app/property_search/forms.py': "# app/property_search/forms.py (Optional search/filter forms)\n",
    'app/property_search/templates/property_search/city_page.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{{ city }} Listings</title>
</head>
<body>
    <h1>Listings for {{ city }}</h1>
    <!-- Display listings here -->
</body>
</html>
""",
    'app/property_search/templates/property_search/search.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Property Search</title>
</head>
<body>
    <h1>Search Properties</h1>
    <!-- Search form and filters here -->
</body>
</html>
""",
    'app/services/__init__.py': """\
# app/services/__init__.py
from flask import Blueprint

services = Blueprint('services', __name__)

from . import routes
""",
    'app/services/routes.py': """\
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
""",
    'app/services/templates/services/buying.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Buying</title>
</head>
<body>
    <h1>Buying Services</h1>
</body>
</html>
""",
    'app/services/templates/services/selling.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Selling</title>
</head>
<body>
    <h1>Selling Services</h1>
</body>
</html>
""",
    'app/services/templates/services/consultation.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Consultation</title>
</head>
<body>
    <h1>Consultation/Market Analysis</h1>
</body>
</html>
""",
    'app/reviews/__init__.py': """\
# app/reviews/__init__.py
from flask import Blueprint

reviews = Blueprint('reviews', __name__)

from . import routes
""",
    'app/reviews/routes.py': """\
# app/reviews/routes.py
from flask import render_template
from . import reviews

@reviews.route('/reviews/video')
def video_testimonials():
    return render_template('reviews/video_testimonials.html')

@reviews.route('/reviews/written')
def written_reviews():
    return render_template('reviews/written_reviews.html')
""",
    'app/reviews/templates/reviews/video_testimonials.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Video Testimonials</title>
</head>
<body>
    <h1>Video Testimonials</h1>
</body>
</html>
""",
    'app/reviews/templates/reviews/written_reviews.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Written Reviews</title>
</head>
<body>
    <h1>Written Reviews</h1>
</body>
</html>
""",
    'app/about/__init__.py': """\
# app/about/__init__.py
from flask import Blueprint

about = Blueprint('about', __name__)

from . import routes
""",
    'app/about/routes.py': """\
# app/about/routes.py
from flask import render_template
from . import about

@about.route('/about/our_story')
def our_story():
    return render_template('about/our_story.html')

@about.route('/about/meet_the_team')
def meet_the_team():
    return render_template('about/meet_the_team.html')
""",
    'app/about/templates/about/our_story.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Our Story</title>
</head>
<body>
    <h1>Our Story</h1>
</body>
</html>
""",
    'app/about/templates/about/meet_the_team.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Meet the Team</title>
</head>
<body>
    <h1>Meet the Team</h1>
</body>
</html>
""",
    'app/resources/__init__.py': """\
# app/resources/__init__.py
from flask import Blueprint

resources = Blueprint('resources', __name__)

from . import routes
""",
    'app/resources/routes.py': """\
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
""",
    'app/resources/templates/resources/market_trends.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Market Trends</title>
</head>
<body>
    <h1>Market Trends</h1>
</body>
</html>
""",
    'app/resources/templates/resources/neighborhood_guides.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Neighborhood Guides</title>
</head>
<body>
    <h1>Neighborhood Guides</h1>
</body>
</html>
""",
    'app/resources/templates/resources/buying_selling_tips.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Buying & Selling Tips</title>
</head>
<body>
    <h1>Buying & Selling Tips</h1>
</body>
</html>
""",
    'app/resources/templates/resources/faq.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>FAQ</title>
</head>
<body>
    <h1>Frequently Asked Questions</h1>
</body>
</html>
""",
    'app/contact/__init__.py': """\
# app/contact/__init__.py
from flask import Blueprint

contact = Blueprint('contact', __name__)

from . import routes
""",
    'app/contact/routes.py': """\
# app/contact/routes.py
from flask import render_template
from . import contact

@contact.route('/contact')
def contact_form():
    return render_template('contact/contact_form.html')

@contact.route('/contact/scheduling')
def scheduling():
    return render_template('contact/scheduling.html')
""",
    'app/contact/forms.py': "# app/contact/forms.py (Contact and appointment scheduling forms)\n",
    'app/contact/templates/contact/contact_form.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Form</h1>
</body>
</html>
""",
    'app/contact/templates/contact/scheduling.html': """\
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Schedule an Appointment</title>
</head>
<body>
    <h1>Appointment Scheduling</h1>
</body>
</html>
""",
    'app/static/css/': None,
    'app/static/js/': None,
    'app/static/images/': None,
    'tests/': None,
}

def create_structure(base_path, structure):
    for path, content in structure.items():
        full_path = os.path.join(base_path, path)
        if content is None:
            # Create a directory
            os.makedirs(full_path, exist_ok=True)
            print(f"Created directory: {full_path}")
        else:
            # Ensure the directory exists
            dir_name = os.path.dirname(full_path)
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name, exist_ok=True)
                print(f"Created directory: {dir_name}")
            # Write the file with the given content
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created file: {full_path}")

if __name__ == "__main__":
    base_dir = os.getcwd()  # assuming you are already in the my_app directory
    create_structure(base_dir, structure)
    print("Project structure created successfully!")
