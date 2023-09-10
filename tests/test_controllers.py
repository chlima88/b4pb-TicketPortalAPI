import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestUserController:
    def test_can_post_users(self):
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

        assert response.status_code == 201
        assert set(data).issubset(set(response.json()))

    def test_cant_post_with_missing_props(self):
        data = {
            "name": "Charles",
            "role": "TI",
            "departmentId": 1,
        }

        response = client.post(
            "/users",
            data=json.dumps(data),
        )

        assert response.status_code == 422

    def test_cant_post_with_blank_props(self):
        data = {
            "name": "Charles",
            "role": "",
            "email": "charles@test.com",
            "departmentId": 1,
        }

        data1 = data
        data1["name"] = ""
        response1 = client.post(
            "/users",
            data=json.dumps(data),
        )

        data2 = data
        data2["role"] = ""
        response2 = client.post(
            "/users",
            data=json.dumps(data),
        )

        data3 = data
        data3["email"] = ""
        response3 = client.post(
            "/users",
            data=json.dumps(data),
        )

        assert response1.status_code == 422
        assert response2.status_code == 422
        assert response3.status_code == 422

    def test_cant_post_user_space_only_props(self):
        data = {
            "name": "Charles",
            "role": "TI",
            "email": "charles@test.com",
            "departmentId": 1,
        }

        data1 = data
        data1["name"] = "  "
        response1 = client.post(
            "/users",
            data=json.dumps(data),
        )

        data2 = data
        data2["role"] = "  "
        response2 = client.post(
            "/users",
            data=json.dumps(data),
        )

        data3 = data
        data3["email"] = "  "
        response3 = client.post(
            "/users",
            data=json.dumps(data),
        )

        assert response1.status_code == 422, "'name' filled out with space"
        assert response2.status_code == 422, "'role' filled out with space"
        assert response3.status_code == 422, "'email' filled out with space"

    def test_can_get_user_by_id(self):
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

        id = response.json()["id"]

        response = client.get(f"/users/{id}")

        assert response.status_code == 200
        assert set(data).issubset(set(response.json()))

    def test_cant_get_user_by_invalid_id(self):
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

        id = -1

        response = client.get(f"/users/{id}")

        assert response.status_code == 400

    def test_can_get_all_users(self):
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
