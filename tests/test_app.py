import os
import pytest
import json
from pss_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get('/')
    assert b"Hello" in rv.data


def test_initial_cookies(client):
    rv = client.post('/addname', data=dict(name='simon'))
    cookies = set()
    for cookie in client.cookie_jar:
        cookies.add((cookie.name, cookie.value))

    expected_cookies = [('name', 'simon'),
                        ('ai_total', '0'),
                        ('user_total', '0'),
                        ('history', '"[]"')]
    
    for expected_cookie in expected_cookies:
        assert expected_cookie in cookies
