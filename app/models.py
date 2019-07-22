from datetime import datetime

from flask_login import UserMixin
from flask_mail import Message
from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        Numeric, String, Text)
from sqlalchemy.orm import relationship

from app import bcrypt, db, mail


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
    billing = relationship('Billing', backref='user')

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"

    @staticmethod
    def generate_password_hash(password):
        return bcrypt.generate_password_hash(password)

    def get_id(self):
        return self.id

    def authenticate(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def send_welcome_message(self):
        message = Message(subject='Welcome', recipients=[self.email])

        message.body = '''
Welcome to finance

Your registration was successful!!!
        '''

        mail.send(message)


class Billing(db.Model):
    id = Column(Integer,
                primary_key=True)
    title = Column(String(250),
                   nullable=False)
    description = Column(Text,
                         nullable=False)
    value = Column(Numeric(10, 2),
                   nullable=False)
    work_date = Column(DateTime,
                       nullable=False,
                       default=datetime.utcnow)
    receive_date = Column(DateTime,
                          nullable=True,
                          default=None)
    received = Column(Boolean,
                      nullable=False,
                      default=False)
    user_id = Column(Integer,
                     ForeignKey('user.id'))

    def __repr__(self):
        return f"<Billing(id={self.id}, title='{self.title}')>"

    def confirm_receive(self):
        self.receive_date = datetime.utcnow()
        self.received = True

    def cancel_receive(self):
        self.receive_date = None
        self.received = False
