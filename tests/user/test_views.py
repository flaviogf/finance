from app.models import User


class TestLogin:
    def test_should_access_login_return_status_200(self, client):
        response = client.get('/login', follow_redirects=True)

        assert 200 == response.status_code

    def test_should_login_return_field_required_when_not_inform_email(self, client):
        data = {
            'email': '',
            'password': 'test123'
        }

        response = client.post('/login', data=data, follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_login_return_field_required_when_not_inform_password(self, client):
        data = {
            'email': 'naruto@gmail.com',
            'password': ''
        }

        response = client.post('/login', data=data, follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_login_return_invalid_email_when_inform_a_email_invalid(self, client):
        data = {
            'email': 'naruto@gmail',
            'password': 'test123'
        }

        response = client.post('/login', data=data, follow_redirects=True)

        assert b'Invalid email address' in response.data

    def test_should_login_return_check_your_email_or_password_when_user_or_password_is_incorrect(self, client, db, bcrypt):
        password = bcrypt.generate_password_hash('test123')

        naruto = User(name='naruto',
                      email='naruto@email.com',
                      password=password)

        db.session.add(naruto)

        db.session.commit()

        data = {
            'email': naruto.email,
            'password': 'wrong password'
        }

        response = client.post('/login', data=data, follow_redirects=True)

        assert b'Check your email or password.' in response.data

    def test_should_login_redirect_to_home_when_user_login(self, client, db, bcrypt):
        password = bcrypt.generate_password_hash('test123')

        naruto = User(name='naruto',
                      email='naruto@email.com',
                      password=password)

        db.session.add(naruto)

        db.session.commit()

        data = {
            'email': naruto.email,
            'password': 'test123'
        }

        response = client.post('/login', data=data, follow_redirects=True)

        assert b'Home' in response.data


class TestRegister:
    def test_should_access_register_return_status_200(self, client):
        response = client.get('/register')

        assert 200 == response.status_code
