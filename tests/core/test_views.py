from datetime import datetime

from app.models import Billing, User


class TestHome:
    def test_should_access_home_return_status_200(self, client):
        response = client.get('/')

        assert 200 == response.status_code

    def test_should_home_return_total_billing_received(self, client, db):
        db.session.add(Billing(title='Billing 1',
                               description='Description billing 1',
                               value=100,
                               work_date=datetime.utcnow(),
                               receive_date=datetime.utcnow(),
                               received=True,
                               user_id=None),)

        db.session.add(Billing(title='Billing 2',
                               description='Description billing 2',
                               value=100,
                               work_date=datetime.utcnow(),
                               receive_date=datetime.utcnow(),
                               received=True,
                               user_id=None),)

        db.session.add(Billing(title='Billing 3',
                               description='Description billing 3',
                               value=100,
                               work_date=datetime.utcnow(),
                               receive_date=datetime.utcnow(),
                               received=True,
                               user_id=1),)

        db.session.add(Billing(title='Billing 4',
                               description='Description billing 4',
                               value=100,
                               work_date=datetime.utcnow(),
                               receive_date=None,
                               received=False,
                               user_id=None),)

        db.session.commit()

        response = client.get('/')

        assert b'R$ 200.00' in response.data


    def test_should_home_return_total_billing_receivable(self, client, db):
        db.session.add(Billing(title='Billing 1',
                               description='Description billing 1',
                               value=100,
                               work_date=datetime.utcnow(),
                               receive_date=None,
                               received=False,
                               user_id=None),)

        db.session.add(Billing(title='Billing 2',
                               description='Description billing 2',
                               value=100,
                               work_date=datetime.utcnow(),
                               receive_date=None,
                               received=False,
                               user_id=None),)

        db.session.add(Billing(title='Billing 3',
                               description='Description billing 3',
                               value=100,
                               work_date=datetime.utcnow(),
                               receive_date=None,
                               received=False,
                               user_id=1),)

        db.session.add(Billing(title='Billing 4',
                               description='Description billing 4',
                               value=100,
                               work_date=datetime.utcnow(),
                               receive_date=datetime.utcnow(),
                               received=True,
                               user_id=None),)

        db.session.commit()

        response = client.get('/')

        assert b'R$ 200.00' in response.data
