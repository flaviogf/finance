from datetime import datetime

from app.models import Billing, User


class TestCreate:
    def test_should_access_create_billing_return_status_200(self, client):
        response = client.get('/billing/create')

        assert 200 == response.status_code

    def test_should_create_return_field_required_when_not_inform_title(self, client):
        data = {
            'title': '',
            'description': 'Description billing one',
            'value': 100.99,
            'work_date': '2019-01-01 12:00:00'
        }

        response = client.post('/billing/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_create_return_field_required_when_not_inform_description(self, client):
        data = {
            'title': 'Billing one',
            'description': '',
            'value': 100.99,
            'work_date': '2019-01-01 12:00:00'
        }

        response = client.post('/billing/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_create_return_field_required_when_not_inform_value(self, client):
        data = {
            'title': 'Billing one',
            'description': 'Description billing one',
            'value': None,
            'work_date': '2019-01-01 12:00:00'
        }

        response = client.post('/billing/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_create_return_min_number_zero_when_inform_number_lower_than_zero(self, client):
        data = {
            'title': 'Billing one',
            'description': 'Description billing one',
            'value': -1,
            'work_date': '2019-01-01 12:00:00'
        }

        response = client.post('/billing/create',
                               data=data,
                               follow_redirects=True)

        assert b'Number must be at least 0' in response.data

    def test_should_create_return_field_required_when_not_inform_work_date(self, client):
        data = {
            'title': 'Billing one',
            'description': 'Description billing one',
            'value': 100.99,
            'work_date': ''
        }

        response = client.post('/billing/create',
                               data=data,
                               follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_create_redirect_to_pagination_when_create_billing(self, client):
        data = {
            'title': 'Billing one',
            'description': 'Description billing one',
            'value': 100.99,
            'work_date': '2019-01-01 12:00:00'
        }

        response = client.post('/billing/create',
                               data=data,
                               follow_redirects=True)

        assert b'Finance - Search Billing' in response.data

    def test_should_create_insert_billing_in_database(self, client):
        data = {
            'title': 'Billing one',
            'description': 'Description billing one',
            'value': 100.99,
            'work_date': '2019-01-01 12:00:00'
        }

        response = client.post('/billing/create',
                               data=data,
                               follow_redirects=True)

        assert 1 == Billing.query.count()


class TestPagination:
    def test_should_access_billing_return_status_200(self, client):
        response = client.get('/billing',
                              follow_redirects=True)

        assert 200 == response.status_code


class TestUpdate:
    def test_should_access_update_return_status_200_when_billing_exists(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow())

        db.session.add(billing)

        db.session.commit()

        response = client.get('billing/1', follow_redirects=True)

        assert 200 == response.status_code

    def test_should_access_update_return_status_404_when_billing_not_exists(self, client):
        response = client.get('billing/1', follow_redirects=True)

        assert 404 == response.status_code

    def test_should_update_billing_return_billing_updated_when_update_billing(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow())

        db.session.add(billing)

        db.session.commit()

        data = {
            'title': 'Updated',
            'description': 'Updated',
            'value': 99.99,
            'work_date': '2019-10-10 10:10:10'
        }

        response = client.post('billing/1', data=data, follow_redirects=True)

        assert b'Billing updated with successfully.' in response.data


class TestConfirmReceive:
    def test_should_confirm_receive_redirect_to_billing_when_confirm_receive(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow())

        db.session.add(billing)

        db.session.commit()

        response = client.get('/billing/1/confirm-receive',
                              follow_redirects=True)

        assert b'Finance - Search Billing' in response.data

    def test_should_confirm_receive_update_receive_date_in_database_when_confirm_receive(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow())

        db.session.add(billing)

        db.session.commit()

        client.get('/billing/1/confirm-receive',
                   follow_redirects=True)

        billing = Billing.query.first()

        assert billing.receive_date

    def test_should_confirm_receive_update_received_in_database_when_confirm_receive(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow())

        db.session.add(billing)

        db.session.commit()

        client.get('/billing/1/confirm-receive',
                   follow_redirects=True)

        billing = Billing.query.first()

        assert billing.received

    def test_should_confirm_receive_with_user_id_not_equals_current_user_id_return_status_forbidden(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=1)

        db.session.add(billing)

        db.session.commit()

        response = client.get('/billing/1/confirm-receive',
                              follow_redirects=True)

        assert 403 == response.status_code


class TestCancelReceive:
    def test_should_cancel_receive_redirect_to_billing_when_cancel_receive(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=None)

        billing.confirm_receive()

        db.session.add(billing)

        db.session.commit()

        response = client.get('/billing/1/cancel-receive',
                              follow_redirects=True)

        assert b'Finance - Search Billing' in response.data

    def test_should_cancel_receive_update_received_data_in_database_when_cancel_receive(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=None)

        billing.confirm_receive()

        db.session.add(billing)

        db.session.commit()

        client.get('/billing/1/cancel-receive',
                   follow_redirects=True)

        billing = Billing.query.first()

        assert not billing.receive_date

    def test_should_cancel_receive_update_received_in_database_when_cancel_receive(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=None)

        billing.confirm_receive()

        db.session.add(billing)

        db.session.commit()

        client.get('/billing/1/cancel-receive',
                   follow_redirects=True)

        billing = Billing.query.first()

        assert not billing.received

    def test_should_cancel_receive_return_status_forbidden_when_billing_user_id_not_equals_current_user_id(self, client, db):
        billing = Billing(title=' Billing one',
                          description=' Description billing one',
                          value=100.99,
                          work_date=datetime.utcnow(),
                          user_id=1)

        billing.confirm_receive()

        db.session.add(billing)

        db.session.commit()

        response = client.get('/billing/1/cancel-receive',
                              follow_redirects=True)

        assert 403 == response.status_code
