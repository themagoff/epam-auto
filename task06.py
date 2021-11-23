import pytest
import requests


@pytest.fixture
def url():
    return "https://reqres.in"


def test_last_name(url):
    r = requests.get(f"{url}/api/users/2")
    last_name = r.json()["data"]["last_name"]
    assert last_name == "Weaver"


def test_not_found_user(url):
    r = requests.get(f"{url}/api/users/23")
    assert r.status_code == 404


def test_add_user(url):
    data = {"name": "alex", "job": "tester"}
    r = requests.post(f"{url}/api/users", data=data)
    assert r.status_code == 201


def test_register_no_email(url):
    data = {"password": "123"}
    r = requests.post(f"{url}/api/register", data=data)
    err_msg = r.json()["error"]
    assert err_msg == "Missing email or username"


def test_success_login(url):
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    r = requests.post(f"{url}/api/login", data=data)
    assert "token" in r.json(), "No token in login response"
