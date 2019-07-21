from app import create_app


class TestApp:
    def test_should_access_app_return_status_ok(self):
        app = create_app()

        client = app.test_client()

        response = client.get('/')

        assert 200 == response.status_code
