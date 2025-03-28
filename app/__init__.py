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
