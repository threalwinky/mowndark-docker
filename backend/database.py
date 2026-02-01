"""
Database connection and initialization for MongoDB
"""

from pymongo import MongoClient
from flask import g

mongo_client = None
db = None

def init_db(app):
    """Initialize MongoDB connection"""
    global mongo_client, db
    
    mongo_client = MongoClient(app.config['MONGODB_URI'])
    db = mongo_client[app.config['MONGODB_DB_NAME']]
    
    # Store db in app context
    app.db = db
    
    # Create indexes
    _create_indexes()
    
    return db

def _create_indexes():
    """Create database indexes for better query performance"""
    global db
    
    if db is not None:
        try:
            # User indexes
            db.users.create_index('email', unique=True, background=True)
            db.users.create_index('username', unique=True, sparse=True, background=True)
            
            # Note indexes - use sparse=True to allow null values
            db.notes.create_index('shortid', unique=True, sparse=True, background=True)
            db.notes.create_index('alias', unique=True, sparse=True, background=True)
            db.notes.create_index('owner_id', background=True)
            db.notes.create_index('created_at', background=True)
            db.notes.create_index('updated_at', background=True)
        except Exception as e:
            print(f"Warning: Index creation issue (may already exist): {e}")

def get_db():
    """Get database instance"""
    global db
    return db

def get_collection(collection_name):
    """Get a specific collection from the database"""
    global db
    if db is not None:
        return db[collection_name]
    return None
