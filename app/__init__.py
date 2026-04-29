from flask import Flask
from app.routes import main

# Creates the Flask app from configuration implemented


def create_app():
    app = Flask(__name__)

    # Basic config
    app.config["SECRET_KEY"] = "dev"

    # Register blueprints
    app.register_blueprint(main)

    return app
