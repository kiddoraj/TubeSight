import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///your_database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = os.environ.get('ENV') or 'development'
    DEBUG = ENV == 'development'
    WTF_CSRF_ENABLED = True
    SESSION_TYPE = 'filesystem'
    LOG_LEVEL = os.environ.get('LOG_LEVEL') or 'DEBUG'
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT') or 'your_password_salt'
    API_KEY = os.environ.get('API_KEY') or 'your_api_key'
    MAX_UPLOAD_SIZE = 10 * 1024 * 1024 # 10 MB

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}