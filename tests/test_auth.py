import pytest
from flask import url_for
from app.models import User


def test_get_register(test_client, test_app):
    """Test registration page access."""
    with test_app.test_request_context():
        response = test_client.get(url_for('main.register'), follow_redirects=True)
        assert response.status_code == 200
        assert b"Username" in response.data
        assert b"Email" in response.data
        assert b"Password" in response.data
        assert b"Sign Up" in response.data
        assert b"Already have an account?" in response.data


def test_get_login(test_client, test_app):
    """Test login page access."""
    with test_app.test_request_context():
        response = test_client.get(url_for('main.login'), follow_redirects=True)
        assert response.status_code == 200
        assert b"Login" in response.data
        assert b"Email" in response.data
        assert b"Password" in response.data
        assert b"Login" in response.data
        assert b"Don't have an account?" in response.data


def test_register(test_client, test_app):
    """Test the registration process."""
    with test_app.test_request_context():
        response = test_client.post(url_for('main.register'), data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password',
            'submit': True
        }, follow_redirects=True)
        print(response.data)
        assert response.status_code == 200
        assert b'Your account has been created!' in response.data


def test_login(test_client, init_database):
    """Test the login process."""
    with test_client:
        response = test_client.post(url_for('main.login'), data={
            'email': 'testuser@example.com',
            'password': 'password',
            'submit': True
        }, follow_redirects=True)
        assert response.status_code == 200
        assert b'You are logged in' in response.data

