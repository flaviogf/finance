from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config='app.config.Development'):
    app = Flask(__name__)
    app.config.from_object(config)

    from app.models import User
    from app.core.views import core
    from app.user.views import user

    db.init_app(app)

    bcrypt.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.user_loader(
        lambda user_id: User.query.get(user_id)
    )

    app.register_blueprint(core)
    app.register_blueprint(user)

    return app
