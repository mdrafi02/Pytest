import pytest
import requests
import json

@pytest.fixture
def main_url():
    return "https://reqres.in"

def test_valid_login(main_url):
    url = main_url + "/api/login/"
    data = {'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
    response = requests.post(url, data=data)
    t = json.loads(response.text)
    assert response.status_code == 200
    assert t['token'] == "QpwL5tke4Pnpja7X4"