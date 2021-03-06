import os
import datetime

class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(hours=12)

class DevelopmentConfig(Config):
    """Configurations for Development.os.getenv gets the variables in development environment"""
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')

class TestingConfig(Config):
    """Configurations for Testing."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv('TESTING_DATABASE_URL')

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False
    DATABASE_URL = os.getenv('DATABASE_URL')

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}