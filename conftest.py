import pytest
import json
from utils.api_client import APIClient

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_client():
    """Fixture zwracająca klienta API."""
    return APIClient(BASE_URL)

@pytest.fixture
def test_data():
    """Fixture zwracająca dane testowe z pliku JSON."""
    with open("data/test_data.json") as f:
        return json.load(f)
