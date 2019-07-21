import pytest

from app import bcrypt as _bcrypt
from app import create_app
from app import db as _db


@pytest.fixture
def app():
    app = create_app('app.config.Testing')
    app.testing = True
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.yield_fixture
def db(app):
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()


@pytest.yield_fixture
def bcrypt(app):
    with app.app_context():
        yield _bcrypt
