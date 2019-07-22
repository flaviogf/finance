from app.models import User
from unittest import mock


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

        assert b'Finance - Home' in response.data


class TestRegister:
    def test_should_access_register_return_status_200(self, client):
        response = client.get('/register')

        assert 200 == response.status_code

    def test_should_register_return_field_required_when_not_inform_name(self, client):
        data = {
            'name': '',
            'email': 'naruto@gmail.com',
            'password': 'sasuke',
            'confirm_password': 'sasuke'
        }

        response = client.post('/register', data=data, follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_register_return_field_required_when_not_inform_email(self, client):
        data = {
            'name': 'naruto',
            'email': '',
            'password': 'sasuke',
            'confirm_password': 'sasuke'
        }

        response = client.post('/register', data=data, follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_register_return_field_required_when_not_inform_password(self, client):
        data = {
            'name': 'naruto',
            'email': 'naruto@gmail.com',
            'password': '',
            'confirm_password': 'sasuke'
        }

        response = client.post('/register', data=data, follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_register_return_field_required_when_not_inform_confirm_password(self, client):
        data = {
            'name': 'naruto',
            'email': 'naruto@gmail.com',
            'password': 'sasuke',
            'confirm_password': ''
        }

        response = client.post('/register', data=data, follow_redirects=True)

        assert b'This field is required' in response.data

    def test_should_register_return_invalid_password_when_confirm_password_not_is_equal_to_password(self, client):
        data = {
            'name': 'naruto',
            'email': 'naruto@gmail.com',
            'password': 'sasuke',
            'confirm_password': 'boruto'
        }

        response = client.post('/register', data=data, follow_redirects=True)

        assert b'Field must be equal to password' in response.data

    def test_should_register_return_email_is_already_in_use_when_email_is_already_in_use(self, client, db):
        naruto = User(name='naruto',
                      email='naruto@gmail.com',
                      password='sasuke')

        db.session.add(naruto)

        db.session.commit()

        data = {
            'name': 'naruto',
            'email': 'naruto@gmail.com',
            'password': 'sasuke',
            'confirm_password': 'sasuke'
        }

        response = client.post('/register', data=data, follow_redirects=True)

        assert b'Email is already in use' in response.data

    def test_should_register_redirect_to_login_when_register_user(self, client):
        data = {
            'name': 'naruto',
            'email': 'naruto@gmail.com',
            'password': 'sasuke',
            'confirm_password': 'sasuke'
        }

        response = client.post('/register', data=data, follow_redirects=True)

        assert b'Finance - Login' in response.data

    def test_should_register_insert_user_in_database(self, client):
        data = {
            'name': 'naruto',
            'email': 'naruto@gmail.com',
            'password': 'sasuke',
            'confirm_password': 'sasuke'
        }

        client.post('/register', data=data, follow_redirects=True)

        assert 1 == User.query.count()


class TestLogout:
    def test_should_logout_redirect_to_login(self, client):
        response = client.get('/logout', follow_redirects=True)

        assert b'Finance - Login' in response.data
