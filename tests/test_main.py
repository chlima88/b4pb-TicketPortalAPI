import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_post_users():
    data = {
        "name": "Charles",
        "role": "TI",
        "email": "charles@test.com",
        "departmentId": 1,
    }

    response = client.post(
        "/users",
        data=json.dumps(data),
    )

    assert response.status_code == 200
    assert set(data).issubset(set(response.json()))


def test_get_user_by_id():
    data = {
        "name": "Charles",
        "role": "TI",
        "email": "charles@test.com",
        "departmentId": 1,
    }

    response = client.post(
        "/users",
        data=json.dumps(data),
    )

    id = -1  # response.json()["id"]

    response = client.get(f"/users/{id}")

    assert response.status_code == 200
    assert set(data).issubset(set(response.json()))


def test_get_all_users():
    data = [
        {
            "name": "Charles",
            "role": "TI",
            "email": "charles@test.com",
            "departmentId": 1,
        },
        {
            "name": "Blenda",
            "role": "RH",
            "email": "Blenda@test.com",
            "departmentId": 5,
        },
    ]

    for user in data:
        client.post(
            "/users",
            data=json.dumps(user),
        )

    response = client.get(f"/users")

    assert response.status_code == 200
