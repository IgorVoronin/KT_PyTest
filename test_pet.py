import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
headers = {"Content-Type": "application/json"}


@pytest.fixture
def pet_data():
    return {
        "id": 1001,
        "name": "Buddy",
        "photoUrls": ["http://example.com/buddy.jpg"],
        "status": "available"
    }


def test_add_new_pet(pet_data):
    response = requests.post(f"{BASE_URL}/pet", json=pet_data, headers=headers)
    assert response.status_code == 200


def test_get_pet_by_id(pet_data):
    response = requests.get(f"{BASE_URL}/pet/{pet_data['id']}")
    assert response.status_code == 200
    assert response.json()["name"] == pet_data["name"]


def test_update_pet(pet_data):
    updated_data = pet_data.copy()
    updated_data["name"] = "Max"
    response = requests.put(
        f"{BASE_URL}/pet", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Max"


def test_delete_pet(pet_data):
    response = requests.delete(f"{BASE_URL}/pet/{pet_data['id']}")
    assert response.status_code == 200


def test_find_pets_by_status():
    response = requests.get(
        f"{BASE_URL}/pet/findByStatus", params={"status": "available"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
