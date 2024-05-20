from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_talisman import Talisman

from app.routes import main
from app.config import config
from app.models import db, User


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['FERNET_KEY'] = config.FERNET_KEY

    db.init_app(app)
    bcrypt = Bcrypt(app)
    login_manager = LoginManager(app)
    migrate = Migrate(app, db)
    talisman = Talisman(app)
    # limiter = Limiter(app, key_func=lambda: current_user.id if current_user.is_authenticated else request.remote_addr)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    login_manager.login_view = 'main.login'
    login_manager.login_message_category = 'info'

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)

    return app
