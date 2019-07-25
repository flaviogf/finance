from os import environ

from app import create_app

app = create_app(config='app.config.Production')
