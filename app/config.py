"""Configurations for the application"""

from logging import getLogger
from app.utils import get_config, generate_md5_hash, generate_random_string

logger = getLogger(__name__)


# pylint: disable=too-few-public-methods
class BaseConfig:
    """Base configuration settings"""

    HOST = get_config("HOST", required=True)
    PORT = get_config("PORT", required=True)
    PORT = get_config("PORT", required=True)
    MYSQL_DATABASE = get_config("MYSQL_DATABASE", required=True)
    MYSQL_USER = get_config("MYSQL_USER", required=True)
    MYSQL_PASSWORD = get_config("MYSQL_PASSWORD", required=True)
    MYSQL_HOST = get_config("MYSQL_HOST", required=True)
    SQLALCHEMY_DATABASE_URI = (
        f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = get_config(
        "SECRET_KEY", default_value=generate_md5_hash(generate_random_string(15))
    )
    SESSION_COOKIE_HTTPONLY = True


# pylint: disable=too-few-public-methods
class DevelopmentConfig(BaseConfig):
    """Settings for the development environment"""

    DEBUG = True
    SESSION_COOKIE_SAMESITE = "Lax"


# pylint: disable=too-few-public-methods
class ProductionConfig(BaseConfig):
    """Settings for the production environment"""

    DEBUG = False
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = "Lax"


app_config = {"development": DevelopmentConfig, "production": ProductionConfig}
