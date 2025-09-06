import requests

class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"} if token else {}

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}{endpoint}", headers=self.headers, params=params)

    def post(self, endpoint, json=None):
        return requests.post(f"{self.base_url}{endpoint}", headers=self.headers, json=json)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)
