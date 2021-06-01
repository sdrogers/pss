import os
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get('/')