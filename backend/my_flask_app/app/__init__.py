from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Initialize SQLAlchemy and JWTManager instances
db = SQLAlchemy()
jwt = JWTManager()

# Define a function to create the Flask application instance
def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    # Initialize SQLAlchemy with the Flask application instance
    db.init_app(app)

    # Initialize JWTManager with the Flask application instance
    jwt.init_app(app)

    # Import and register blueprints (routes) from app package
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    from app.auth import auth_bp
    app.register_blueprint(auth_bp)

    # Return the Flask application instance
    return app