import pytest
import json
from app import app


@pytest.fixture
def client():
    client = app.test_client()
    yield client


def test_signup(client):
    test_data = {"username" :"test100", "password" : "test"}
    rv = client.post('/auth/signup/', data=json.dumps(test_data), content_type = 'application/json')
    assert 200 == rv.status_code

def test_login(client):
    test_data = {"username": "test3", "password": "test"}
    rv = client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
    assert 200 == rv.status_code
    assert b'access_token' in rv.data


def test_post(client):
    test_data = {"username": "test3", "password": "test"}
    rv = client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
    json_data = rv.get_json()
    access_token = json_data["access_token"]
    test_data2 = {"subject": "test3", "content": "test"}
    rv = client.post('/create/', data=json.dumps(test_data2), content_type='application/json',
                     headers={"Authorization": "Bearer {}".format(access_token)})
    assert 200 == rv.status_code


def test_base_route(client):
    url = '/'
    response = client.get(url)
    assert  200 ==response.status_code


def test_base_route(client):
    url = '/detail/1/'
    response = client.get(url)
    assert 200 == response.status_code


def test_modify(client):
    test_data = {"username": "test3", "password": "test"}
    rv = client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
    json_data = rv.get_json()
    access_token = json_data["access_token"]
    test_data2 = {"subject": "modify", "content": "test"}
    rv = client.patch('/modify/1', data=json.dumps(test_data2), content_type='application/json',
                      headers={"Authorization": "Bearer {}".format(access_token)})
    assert 200 == rv.status_code


def test_delete(client):
    test_data = {"username": "test3", "password": "test"}
    rv = client.post('/auth/login/', data=json.dumps(test_data), content_type='application/json')
    json_data = rv.get_json()
    access_token = json_data["access_token"]
    rv = client.delete('/delete/1', headers={"Authorization": "Bearer {}".format(access_token)})
    assert 200 == rv.status_code
