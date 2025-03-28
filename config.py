# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    # Add your configuration variables (e.g., database URIs, API keys) here
