import pytest
from flask import url_for

from app import create_app, db
from app.models import User


@pytest.fixture(scope='module')
def test_app():
    test_config = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': "sqlite:///test.db",
        'WTF_CSRF_ENABLED': False,
        # 'SERVER_NAME': "127.0.0.1:5000",
        'APPLICATION_ROOT': "/",
        'PREFERRED_URL_SCHEME': "http"
    }
    test_application = create_app(test_config)

    print(test_application.config.values())
    with test_application.app_context():
        db.create_all()
        yield test_application
        db.drop_all()
        db.session.remove()


@pytest.fixture(scope='module')
def test_client(test_app):
    return test_app.test_client()


@pytest.fixture(scope='module')
def init_database(test_app):
    with test_app.app_context():
        user = User(username='testuser', email='testuser@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        yield db
        db.session.remove()
        db.drop_all()


@pytest.fixture(scope='function')
def authenticated_client(test_client, test_app):
    response = test_client.post(url_for('main.login'), data={
        'email': 'testuser@example.com',
        'password': 'password',
        'submit': True
    }, follow_redirects=True)
    return test_client
