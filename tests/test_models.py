from app.models import User


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
