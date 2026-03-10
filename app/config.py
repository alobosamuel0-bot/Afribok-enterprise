import os

# Core Configuration Module

class Config:
    # Environment Variables
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1']

    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'default_jwt_secret'
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 3600))  # in seconds

    # Application Settings
    APP_NAME = os.environ.get('APP_NAME') or 'My Application'
    APP_VERSION = os.environ.get('APP_VERSION') or '1.0.0'
