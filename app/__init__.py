"""Initialize the Flask application.

This module provides a factory function to create and configure 
a Flask app instance.

Attributes:
    create_app: Function that creates and configures the Flask 
        app instance.

Example:
    To create the Flask app instance:
    >>> from app import create_app
    >>> app = create_app()
"""

from logging import getLogger
from typing import Optional
from flask import Flask

from app.config import app_config
from app.views import views_bp


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

    app.register_blueprint(views_bp)

    logger.debug("%s configurations loaded successfully.", environment.capitalize())

    return app
