def test_login_success():
    from tests.conftest import client

    response = client.post(
        "/auth/login",
        data={
            "username": "testuser",
            "password": "testpass"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
