class TestHome:
    def test_should_access_home_return_status_200(self, client):
        response = client.get('/')

        assert 200 == response.status_code
