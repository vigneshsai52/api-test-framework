from utils import api_client

class TestUsers:

    def test_get_users_returns_200(self):
        response = api_client.get("/users")
        assert response.status_code == 200

    def test_single_user_returns_200(self):
        response = api_client.get("/users/1")
        assert response.status_code == 200