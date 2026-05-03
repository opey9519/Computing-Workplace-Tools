# tests/test_app.py

import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_route(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["message"] == "CI/CD Notification System Running"


def test_create_notification(client):
    response = client.post("/notifications", json={"message": "Test notification"})

    assert response.status_code == 201
    assert response.json["id"] == 1
    assert response.json["message"] == "Test notification"


def test_create_notification_requires_message(client):
    response = client.post("/notifications", json={})

    assert response.status_code == 400
    assert response.json["error"] == "Message is required"


def test_get_notifications(client):
    client.post("/notifications", json={"message": "First notification"})
    client.post("/notifications", json={"message": "Second notification"})

    response = client.get("/notifications")

    assert response.status_code == 200
    assert len(response.json) >= 2


def test_update_notification(client):
    create_response = client.post("/notifications", json={"message": "Old message"})
    notification_id = create_response.json["id"]

    update_response = client.put(
        f"/notifications/{notification_id}",
        json={"message": "Updated message"}
    )

    assert update_response.status_code == 200
    assert update_response.json["message"] == "Updated message"


def test_update_notification_not_found(client):
    response = client.put("/notifications/999", json={"message": "Updated message"})

    assert response.status_code == 404
    assert response.json["error"] == "Notification not found"


def test_delete_notification(client):
    create_response = client.post("/notifications", json={"message": "Delete me"})
    notification_id = create_response.json["id"]

    delete_response = client.delete(f"/notifications/{notification_id}")

    assert delete_response.status_code == 200
    assert delete_response.json["message"] == "Notification deleted"


def test_delete_notification_not_found(client):
    response = client.delete("/notifications/999")

    assert response.status_code == 404
    assert response.json["error"] == "Notification not found"