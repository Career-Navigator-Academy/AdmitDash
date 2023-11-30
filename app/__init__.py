"""Initialize the Flask application.

This module contains functions and objects to manage Flask app creation.

Functions:
    create_app: Factory function to create and configure a Flask app instance 
        based on the specified environment.
    
Example:
    To create the Flask app instance:
    >>> from app import create_app
    >>> app = create_app()
"""

from logging import getLogger
from typing import Optional
from flask import Flask
from sqlalchemy_utils import database_exists, create_database

from .config import app_config
from .routes import v1
from .models import db
from . import views

logger = getLogger(__name__)


def create_app(environment: Optional[str] = "development") -> Flask:
    """Create and configure the Flask instance based on environment.

    Args:
        environment: The configuration environment to set up the
            Flask application. Default is 'development'.

    Returns:
        Flask: Configured Flask application instance.
    """

    app = Flask(__name__)
    app.config.from_object(app_config[environment])

    app.register_blueprint(views.blueprint)
    app.register_blueprint(v1.blueprint, url_prefix="/v1")

    logger.debug("%s configurations loaded successfully.", environment.capitalize())

    db_url = app.config["SQLALCHEMY_DATABASE_URI"]
    db_name = app.config["MYSQL_DATABASE"]

    if not database_exists(db_url):
        create_database(db_url)

        logger.debug("'%s' database created successfully.", db_name)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
