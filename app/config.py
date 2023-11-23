"""Configurations for the application"""

from logging import getLogger
from app.utils import get_config

logger = getLogger(__name__)


# pylint: disable=too-few-public-methods
class BaseConfig:
    """Base configuration settings"""

    DEBUG = False
    HOST = get_config("HOST", required=True)
    PORT = get_config("PORT", required=True)


# pylint: disable=too-few-public-methods
class DevelopmentConfig(BaseConfig):
    """Settings for the development environment"""

    DEBUG = True


# pylint: disable=too-few-public-methods
class ProductionConfig(BaseConfig):
    """Settings for the production environment"""


app_config = {"development": DevelopmentConfig, "production": ProductionConfig}
