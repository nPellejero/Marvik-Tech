import os
import tempfile

import pytest

from timeAPI import create_app

from datetime import datetime

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def post_now(client, tf):
    return client.post('/time/now', data=dict(
        timeFormat=tf,
    ), follow_redirects=True)

def test_now_true(client):
    rv = post_now(client, True)
    now = datetime.now()
    assert bytes(now.strftime("%Y-%m-%d %H:%M:%S"),'utf-8')  == rv.data
def test_now_false(client):
    rv = post_now(client, False)
    now = datetime.now()
    assert bytes(now.strftime("%Y-%m-%d"),'utf-8')  == rv.data

