import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"
headers = {"Content-Type": "application/json"}


@pytest.fixture
def order_data():
    return {
        "id": 3001,
        "petId": 1001,
        "quantity": 1,
        "shipDate": "2025-04-13T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }


def test_place_order(order_data):
    response = requests.post(
        f"{BASE_URL}/store/order", json=order_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == order_data["id"]


def test_get_order_by_id(order_data):
    response = requests.get(f"{BASE_URL}/store/order/{order_data['id']}")
    assert response.status_code == 200
    assert response.json()["status"] == "placed"


def test_delete_order(order_data):
    response = requests.delete(f"{BASE_URL}/store/order/{order_data['id']}")
    assert response.status_code == 200


def test_get_inventory():
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_nonexistent_order():
    response = requests.get(f"{BASE_URL}/store/order/999999")
    assert response.status_code == 404
