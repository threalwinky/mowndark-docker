"""
Route registration for the Mowndark API
"""

from flask import jsonify
from routes.auth import auth_bp
from routes.notes import notes_bp
from routes.users import users_bp
from routes.status import status_bp
from routes.images import images_bp

def register_routes(app):
    """Register all application routes"""
    
    # API prefix
    api_prefix = '/api'
    
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix=f'{api_prefix}/auth')
    app.register_blueprint(notes_bp, url_prefix=f'{api_prefix}/notes')
    app.register_blueprint(users_bp, url_prefix=f'{api_prefix}/users')
    app.register_blueprint(status_bp, url_prefix=f'{api_prefix}/status')
    app.register_blueprint(images_bp, url_prefix=f'{api_prefix}/images')
    
    # Root route
    @app.route('/')
    def index():
        return jsonify({
            'name': 'Mowndark API',
            'version': '1.0.0',
            'description': 'Markdown Editor Backend'
        })
    
    # Health check
    @app.route('/health')
    def health():
        return jsonify({'status': 'healthy'})
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def server_error(e):
        return jsonify({'error': 'Internal server error'}), 500
