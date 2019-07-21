from flask_login import UserMixin
from sqlalchemy import Column, Integer, String

from app import bcrypt, db


class User(db.Model, UserMixin):
    id = Column(Integer,
                primary_key=True)
    name = Column(String,
                  nullable=False)
    email = Column(String,
                   nullable=False,
                   unique=True)
    image = Column(String,
                   nullable=False,
                   default='default.jpg')
    password = Column(String,
                      nullable=False)

    @staticmethod
    def generate_password_hash(password):
        return bcrypt.generate_password_hash(password)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password, password)
