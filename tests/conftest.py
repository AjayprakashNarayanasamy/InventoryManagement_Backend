import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.fixture(scope="session")
def auth_token():
    client.post(
        "/auth/register",
        data={
            "username": "testuser",
            "password": "testpass"
        }
    )


    response = client.post(
        "/auth/login",
        data={
            "username": "testuser",
            "password": "testpass"
        }
    )

    assert response.status_code == 200

    return response.json()["access_token"]
