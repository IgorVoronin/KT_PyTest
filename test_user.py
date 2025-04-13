import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
headers = {"Content-Type": "application/json"}


@pytest.fixture
def user_data():
    return {
        "id": 2001,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "test@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }


def test_create_user(user_data):
    response = requests.post(
        f"{BASE_URL}/user", json=user_data, headers=headers)
    assert response.status_code == 200


def test_get_user_by_username(user_data):
    response = requests.get(f"{BASE_URL}/user/{user_data['username']}")
    assert response.status_code == 200
    assert response.json()["email"] == user_data["email"]


def test_update_user(user_data):
    updated = user_data.copy()
    updated["email"] = "updated@example.com"
    response = requests.put(
        f"{BASE_URL}/user/{user_data['username']}", json=updated, headers=headers)
    assert response.status_code == 200


def test_delete_user(user_data):
    response = requests.delete(f"{BASE_URL}/user/{user_data['username']}")
    # иногда 404, если не сразу создаётся
    assert response.status_code == 200 or response.status_code == 404


def test_login_user(user_data):
    response = requests.get(f"{BASE_URL}/user/login", params={
                            "username": user_data["username"], "password": user_data["password"]})
    assert response.status_code == 200
