from core.api.http_client import HttpClient


class AuthServices:

    def __init__(self):
        self.http_client = HttpClient()

    def get_token(self, email, password):
        payload = {"email": email, "password": password}
        response = self.http_client.post("auth/login", payload)
        return response.get("access_token")
