"""Initialize the Flask application and Database.

This module contains functions and objects to manage Flask app creation 
and database initialization.

Functions:
    create_app: Factory function to create and configure a Flask app instance 
        based on the specified environment.
    
Objects:
    db: SQLAlchemy object used for managing the database.

Example:
    To create the Flask app instance:
    >>> from app import create_app, db
    >>> app = create_app()
"""

from logging import getLogger
from typing import Optional
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy_utils import database_exists, create_database

from app.config import app_config
from app.views import views_blueprint
from app.api import v1_blueprint

logger = getLogger(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


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

    app.register_blueprint(views_blueprint)
    app.register_blueprint(v1_blueprint, url_prefix="/v1")

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
