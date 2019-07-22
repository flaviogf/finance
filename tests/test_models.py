from datetime import datetime

from app.models import Billing, User


class TestUser:
    def test_should_repr_return_repr_user(self):
        naruto = User(name='naruto',
                      email='naruto@gmail.com',
                      password='sasuke')

        expected = "<User(id=None, name='naruto')>"

        result = repr(naruto)

        assert expected == result

    def test_should_generate_password_hash_return_password_hash(self, bcrypt):
        password = 'xpto'

        password_hash = User.generate_password_hash(password)

        assert bcrypt.check_password_hash(password_hash, password)

    def test_should_authenticate_return_true_when_check_password_hash(self, bcrypt):
        password_hash = bcrypt.generate_password_hash('sasuke')

        naruto = User(name='naruto',
                      email='naruto@gmail.com',
                      password=password_hash)

        password = 'sasuke'

        assert naruto.authenticate(password)

    def test_should_authenticate_return_false_when_not_check_password_hash(self, bcrypt):
        password_hash = bcrypt.generate_password_hash('sasuke')

        naruto = User(name='naruto',
                      email='naruto@gmail.com',
                      password=password_hash)

        password = 'boruto'

        assert not naruto.authenticate(password)


class TestBilling:
    def test_should_repr_return_billing_repr(self):
        billing = Billing(title='Mission A',
                          description='Mission A description',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=1)

        expected = "<Billing(id=None, title='Mission A')>"

        result = repr(billing)

        assert expected == result

    def test_confirm_receive_update_receive_date(self):
        billing = Billing(title='Mission A',
                          description='Mission A description',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=1)

        billing.confirm_receive()

        assert billing.receive_date

    def test_confirm_receive_update_received(self):
        billing = Billing(title='Mission A',
                          description='Mission A description',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=1)

        billing.confirm_receive()

        assert billing.received

    def test_cancel_receive_update_receive_data(self):
        billing = Billing(title='Mission A',
                          description='Mission A description',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=1)

        billing.confirm_receive()

        billing.cancel_receive()

        assert not billing.receive_date

    def test_cancel_receive_update_receive(self):
        billing = Billing(title='Mission A',
                          description='Mission A description',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=1)

        billing.confirm_receive()

        billing.cancel_receive()

        assert not billing.received
