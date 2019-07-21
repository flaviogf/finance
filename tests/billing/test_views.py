class TestBilling:
    def test_should_access_create_billing_return_status_200(self, client):
        response = client.get('/billing/create')

        assert 200 == response.status_code
