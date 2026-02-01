"""
Mowndark - Markdown Editor Backend
A Flask-based API for collaborative markdown editing
"""

import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from config import Config
from database import init_db
from routes import register_routes

# Load environment variables
load_dotenv()

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    CORS(app, origins=["http://localhost:3000", "https://mowndark.vercel.app"], supports_credentials=True)
    JWTManager(app)
    
    # Initialize database
    init_db(app)
    
    # Register routes
    register_routes(app)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
