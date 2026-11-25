
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config


# Initialize SQLAlchemy
db = SQLAlchemy()


def create_app():
    # Create Flask application
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Temporary homepage route
    @app.route("/")
    def home():
        return "Hello, Expense Tracker is running!"

    return app
