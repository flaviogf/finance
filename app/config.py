from os import environ


class Config:
    SECRET_KEY = '7f355bd0a2261318dad660052014a8a49a95e9ce7293d6a9f6ad574f715d57db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
