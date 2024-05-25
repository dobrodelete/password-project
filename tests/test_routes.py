import pytest
from flask import url_for


def test_home_page(authenticated_client):
    """Test the home page for logged-in users."""
    response = authenticated_client.get(url_for('main.home'))
    assert response.status_code == 200
    assert b'Generate a New Password' in response.data


def test_account_page(authenticated_client):
    """Test the account details page."""
    response = authenticated_client.get(url_for('main.account'), )
    assert response.status_code == 200
    assert b'Account Details' in response.data


def test_passwords_page(authenticated_client):
    """Test the passwords management page."""
    response = authenticated_client.get(url_for('main.passwords'))
    assert response.status_code == 200
    assert b'My Passwords' in response.data
