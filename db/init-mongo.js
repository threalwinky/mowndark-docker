// MongoDB initialization script for Mowndark markdown editor

db = db.getSiblingDB('mowndark');

// Create collections
db.createCollection('users');
db.createCollection('notes');

// Create indexes for better query performance
db.users.createIndex({ "email": 1 }, { unique: true });
db.users.createIndex({ "username": 1 }, { unique: true });
db.notes.createIndex({ "owner_id": 1 });
db.notes.createIndex({ "shortid": 1 }, { unique: true });
db.notes.createIndex({ "alias": 1 }, { sparse: true });
db.notes.createIndex({ "created_at": -1 });
db.notes.createIndex({ "updated_at": -1 });

print('MongoDB initialized successfully for Mowndark!');
