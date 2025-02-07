# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize database instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('app.config.Config')
    
    # Initialize database with app
    db.init_app(app)
    
    # Register Blueprints (modular routes)
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
