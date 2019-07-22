from app.models import Billing


class TestBilling:
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

        assert b'Search Billing' in response.data

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

    def test_should_access_billing_return_status_200(self, client):
        response = client.get('/billing')

        assert 200 == response.status_code
