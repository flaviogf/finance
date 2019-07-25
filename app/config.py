from os import environ


class Config:
    SECRET_KEY = '7f355bd0a2261318dad660052014a8a49a95e9ce7293d6a9f6ad574f715d57db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_DEFAULT_SENDER = 'noreply@finance.com'


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    LOGIN_DISABLED = True
    TESTING = True
