"""
Configuration settings for the Mowndark backend
"""

import os
from datetime import timedelta

class Config:
    """Application configuration class"""
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-me')
    DEBUG = os.environ.get('FLASK_ENV') == 'development'
    
    # JWT settings
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key-change-me')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    
    # MongoDB settings
    MONGODB_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/mowndark')
    MONGODB_DB_NAME = 'mowndark'
    
    # Application settings
    ALLOW_ANONYMOUS = True
    DEFAULT_PERMISSION = 'editable'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
    
    # Permission types (similar to CodiMD)
    PERMISSION_TYPES = ['freely', 'editable', 'limited', 'locked', 'protected', 'private']
