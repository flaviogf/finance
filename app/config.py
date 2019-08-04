class Config:
    SECRET_KEY = '7f355bd0a2261318dad660052014a8a49a95e9ce7293d6a9f6ad574f715d57db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    MAIL_DEFAULT_SENDER = 'noreply@finance.com'
    MAIL_USERNAME = 'flavio.fernandes6@gmail.com'
    MAIL_PASSWORD = '3z3G//Ks'


class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@localhost/finance'


class Testing(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    LOGIN_DISABLED = True
    TESTING = True
